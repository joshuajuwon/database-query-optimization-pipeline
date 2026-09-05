-- Create the main sales table
CREATE TABLE sales (
    sale_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    sale_date TIMESTAMP NOT NULL
);