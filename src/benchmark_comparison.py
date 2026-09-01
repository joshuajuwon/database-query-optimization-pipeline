from database_utils import get_connection


QUERY = """
SELECT *
FROM sales
WHERE customer_id = 5000;
"""


def get_execution_time():
    """Run EXPLAIN ANALYZE and return execution time in milliseconds."""
    conn = get_connection()
    cur = conn.cursor()

    explain_query = f"""
    EXPLAIN (ANALYZE, FORMAT JSON)
    {QUERY}
    """

    cur.execute(explain_query)
    result = cur.fetchone()[0]

    execution_time = result[0]["Execution Time"]

    cur.close()
    conn.close()

    return execution_time


def drop_index():
    """Remove the customer_id index."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DROP INDEX IF EXISTS idx_sales_customer_id;")

    conn.commit()
    cur.close()
    conn.close()


def create_index():
    """Create an index on customer_id."""
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_sales_customer_id
        ON sales(customer_id);
    """)

    conn.commit()
    cur.close()
    conn.close()


def main():
    print("DATABASE QUERY OPTIMIZATION BENCHMARK")
    print("=" * 45)

    # Test without index
    print("\nTesting BEFORE optimization...")

    drop_index()

    before_time = get_execution_time()

    print(f"Before index: {before_time:.3f} ms")

    # Create index
    print("\nCreating index...")

    create_index()

    # Test with index
    print("Testing AFTER optimization...")

    after_time = get_execution_time()

    print(f"After index:  {after_time:.3f} ms")

    # Calculate improvement
    speedup = before_time / after_time
    reduction = ((before_time - after_time) / before_time) * 100

    print("\nRESULT")
    print("-" * 45)
    print(f"Before: {before_time:.3f} ms")
    print(f"After:  {after_time:.3f} ms")
    print(f"Speedup: {speedup:.2f}x faster")
    print(f"Execution time reduction: {reduction:.2f}%")


if __name__ == "__main__":
    main()