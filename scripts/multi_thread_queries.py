import mysql.connector
import threading

def execute_query(query):
    conn = mysql.connector.connect(
        host="127.0.0.1",
        user="developer",
        password="${{ secrets.DATABASEPASSWORD }}",
        database="project_db"
    )
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"results from query {query}: {results}")
    conn.commit()
    cursor.close()
    conn.close()

queries = [
    "SELECT * FROM ClimateData WHERE temperature > 20",
    "INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity) VALUES ('New York', '2025-01-18', 22.1, 12.3, 68.5)",
    "UPDATE ClimateData SET humidity = 75 WHERE location = 'London'"
]

threads = []

for query in queries:
    thread = threading.Thread(target=execute_query, args=(query,))
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join()