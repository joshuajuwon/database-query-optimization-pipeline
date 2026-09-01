-- Create an index to optimize customer searches
CREATE INDEX idx_sales_customer_id
ON sales(customer_id);