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
- Compare the results and document the improvement.

## Technologies

- **Python**
- **PostgreSQL**
- **SQL**
- **psycopg2**
- **Pandas**
- **NumPy**
- **Git & GitHub**
