import mysql.connector
import os

# Load environment variables from .secrets file
def load_secrets(file_path=".secrets"):
    if os.path.exists(file_path):
        with open(file_path) as f:
            for line in f:
                if not line.strip().startswith("#") and "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ[key.strip()] = value.strip()

# Load secrets
load_secrets()

# MySQL Connection Configuration using GitHub Secrets Simulation
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME")
}

# SQL Migration Files Directory
MIGRATIONS_DIR = "./sql"

def apply_migrations():
    """Applies all new SQL migration files in order."""
    try:
        # Establish database connection
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Create migration tracking table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS schema_migrations (
                id INT AUTO_INCREMENT PRIMARY KEY,
                filename VARCHAR(255) UNIQUE
            )
        """)
        conn.commit()

        # Retrieve applied migrations
        cursor.execute("SELECT filename FROM schema_migrations")
        applied_migrations = {row[0] for row in cursor.fetchall()}

        # Apply unapplied migration files
        for file in sorted(os.listdir(MIGRATIONS_DIR)):
            if file.endswith(".sql") and file not in applied_migrations:
                print(f"Applying migration: {file}")
                with open(os.path.join(MIGRATIONS_DIR, file), "r") as f:
                    sql_commands = f.read()

                try:
                    for statement in sql_commands.split(";"):
                        if statement.strip():
                            cursor.execute(statement)

                    # Log migration
                    cursor.execute("INSERT INTO schema_migrations (filename) VALUES (%s)", (file,))
                    conn.commit()
                    print(f"Migration {file} applied successfully.")

                except mysql.connector.Error as err:
                    conn.rollback()
                    print(f"Error applying {file}: {err}")
                    break  # Stop on first failure

        cursor.close()
        conn.close()
        print("Database migrations completed.")
    
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")

if __name__ == "__main__":
    apply_migrations()
