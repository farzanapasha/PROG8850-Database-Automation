import mysql.connector
import threading
import os
import time
import sys

def execute_query(query_type, query):
    conn = mysql.connector.connect(
        host=os.environ.get('DB_HOST', '127.0.0.1'),
        user=os.environ.get('DB_USER', 'developer'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        database=os.environ.get('DB_NAME', 'project_db'),
        connection_timeout=10
    )
    
    cursor = conn.cursor()
    print(f"Executing {query_type} query: {query}")
    cursor.execute(query)
    
    if query_type == "SELECT":
        results = cursor.fetchall()
        print(f"Results from {query_type} query: {results}")
    else:
        affected_rows = cursor.rowcount
        conn.commit()
        print(f"{query_type} query affected {affected_rows} rows")
        
    cursor.close()
    conn.close()
    print(f"{query_type} query executed successfully")
    return True
            

queries = [
    ("SELECT", "SELECT * FROM ClimateData WHERE temperature > 20"),
    ("INSERT", "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('New York', '2025-01-18', 22.1, 12.3, 68.5)"),
    ("UPDATE", "UPDATE ClimateData SET humidity = 75 WHERE location = 'London'")
]

def main():
    print("Starting concurrent query execution")
    
    threads = []
    
    for query_type, query in queries:
        thread = threading.Thread(
            target=execute_query, 
            args=(query_type, query),
            name=f"{query_type}-Thread"
        )
        threads.append(thread)
        thread.start()
        print(f"Started thread for {query_type} query")
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
        print(f"Thread {thread.name} completed")
    
    print("All threads completed execution")

if __name__ == "__main__":
    main()