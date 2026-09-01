import time
from database_utils import get_connection


def benchmark_query(runs=5):
    times = []

    for run in range(1, runs + 1):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        SELECT *
        FROM sales
        WHERE customer_id = 5000;
        """

        start_time = time.perf_counter()

        cur.execute(query)
        rows = cur.fetchall()

        end_time = time.perf_counter()

        elapsed = end_time - start_time
        times.append(elapsed)

        print(f"Run {run}: {elapsed:.6f} seconds | Rows: {len(rows)}")

        cur.close()
        conn.close()

    average_time = sum(times) / len(times)

    print("\nBenchmark Summary")
    print("-----------------")
    print(f"Runs: {runs}")
    print(f"Average execution time: {average_time:.6f} seconds")


if __name__ == "__main__":
    benchmark_query()