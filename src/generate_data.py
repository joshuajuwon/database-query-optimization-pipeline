import os
import numpy as np
import pandas as pd

# Make results reproducible
np.random.seed(42)

# Number of records
n_records = 500_000

# Generate sample sales data
df = pd.DataFrame(
    {
        "sale_id": np.arange(1, n_records + 1),
        "customer_id": np.random.randint(1, 10_001, n_records),
        "product_id": np.random.randint(1, 5_001, n_records),
        "quantity": np.random.randint(1, 11, n_records),
        "unit_price": np.round(np.random.uniform(5, 500, n_records), 2),
        "sale_date": pd.date_range(
            start="2023-01-01", periods=n_records, freq="min"
        ),
    }
)

# Output path inside the current project directory
output_dir = "data"
output_file = f"{output_dir}/sales_data.csv"

# Automatically create the 'data' folder if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Save to CSV
df.to_csv(output_file, index=False)

print(f"Dataset created successfully: {output_file}")
print(f"Number of records: {len(df):,}")
print(df.head())