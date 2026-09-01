import psycopg2  # or your preferred database driver/pandas import

DB_CONFIG = {
    "dbname": "query_optimization_db",  # Ensure dbname contains only the database name, not the connection string path
    "user": "postgres",
    "password": "jayone",
    "host": "localhost",
    "port": "5433",
}

def load_data():
    # Add your data loading logic here
    print("Loading data into PostgreSQL...")
    # conn = psycopg2.connect(**DB_CONFIG)
    # ...

if __name__ == "__main__":
    load_data()