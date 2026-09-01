import time
from database_utils import get_connection


def run_query():
    conn = get_connection()
    cur = conn.cursor()

    query = """
    SELECT *
    FROM sales
    WHERE customer_id = 5000;
    """

    start_time = time.time()

    cur.execute(query)
    rows = cur.fetchall()

    end_time = time.time()

    print(f"Rows fetched: {len(rows)}")
    print(f"Execution time: {end_time - start_time:.6f} seconds")

    cur.close()
    conn.close()


if __name__ == "__main__":
    run_query()