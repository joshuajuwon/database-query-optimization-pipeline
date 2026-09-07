# Database Query Optimization Pipeline

A practical PostgreSQL database optimization project demonstrating how indexing can significantly improve SQL query performance.

## Project Overview

This project analyzes and improves the performance of customer search queries using PostgreSQL and Python.

A synthetic sales dataset containing **500,000 records** was generated and stored in PostgreSQL. The project establishes a baseline query performance, creates an index on `customer_id`, and measures the resulting performance improvement using `EXPLAIN ANALYZE` and Python-based benchmarking.

## Objectives

- Generate a large-scale sales dataset for database performance testing.
- Store and query the data using PostgreSQL.
- Measure query performance before optimization.
- Apply indexing to improve query performance.
- Measure performance after optimization.
- Compare and document the performance improvement.

## Technologies

- **Python**
- **PostgreSQL**
- **SQL**
- **psycopg2**
- **Pandas**
- **NumPy**
- **Git & GitHub**




## Query Optimization Results

The performance of a customer search query was measured before and after creating an index on `customer_id`.

| Metric | Before Index | After Index |
|---|---:|---:|
| Execution Time | 4,500.323 ms | 64.942 ms |

### Performance Improvement

- **69.30× faster** query execution
- **98.56% reduction** in execution time
- Index created: `idx_sales_customer_id`
- Query tested: `customer_id = 5000`

### Performance Chart

![Query execution time before and after indexing](results/query_optimization_chart.png)

### Benchmark Query

```sql
EXPLAIN ANALYZE
SELECT *
FROM sales
WHERE customer_id = 5000;
