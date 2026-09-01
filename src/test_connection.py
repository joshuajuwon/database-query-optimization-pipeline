import psycopg2

try:
    conn = psycopg2.connect(
        dbname="query_optimization_db",
        user="postgres",
        password="jayone",
        host="localhost",
        port="5433"
    )

    print("Connection successful!")
    conn.close()

except Exception as e:
    print("Error:", e)