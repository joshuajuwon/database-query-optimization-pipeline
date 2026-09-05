-- Create an index to optimize customer_id search queries
CREATE INDEX idx_sales_customer_id
ON sales(customer_id);