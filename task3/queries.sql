-- Create orders table
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT NOT NULL,
    amount REAL NOT NULL,
    order_date DATE NOT NULL
);

-- Insert sample data
INSERT INTO orders (customer, amount, order_date) VALUES
    ('Alice', 5000, '2024-03-01'),
    ('Bob', 3000, '2024-03-05'),
    ('Alice', 15000, '2024-03-10'),
    ('Charlie', 2000, '2024-03-15'),
    ('Bob', 2000, '2024-03-20');

-- 1. Total Sales for March 2024
SELECT SUM(amount) as total_sales
FROM orders
WHERE strftime('%Y-%m', order_date) = '2024-03';

-- 2. Top Customer Analysis
SELECT 
    customer,
    SUM(amount) as total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;

-- 3. Average Order Value
SELECT AVG(amount) as average_order_value
FROM orders; 