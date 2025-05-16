# SQL Queries: Analyzing a Database Online

## Table Setup

```sql
CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    customer TEXT,
    amount REAL,
    order_date DATE
);

INSERT INTO orders (customer, amount, order_date) VALUES
('Alice', 5000, '2024-03-01'),
('Bob', 8000, '2024-03-05'),
('Alice', 3000, '2024-03-15'),
('Charlie', 7000, '2024-02-20'),
('Alice', 10000, '2024-02-28'),
('Bob', 4000, '2024-02-10'),
('Charlie', 9000, '2024-03-22'),
('Alice', 2000, '2024-03-30');
```

---

## 1. Calculate the total sales volume for March 2024

```sql
SELECT SUM(amount) AS total_sales_march
FROM orders
WHERE strftime('%Y-%m', order_date) = '2024-03';
```
**Expected Result:**

| total_sales_march |
|-------------------|
| 27000             |

---

## 2. Find the customer who spent the most overall

```sql
SELECT customer, SUM(amount) AS total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;
```
**Expected Result:**

| customer | total_spent |
|----------|-------------|
| Alice    | 20000       |

---

## 3. Calculate the average order value for the last three months

```sql
SELECT ROUND(SUM(amount) * 1.0 / COUNT(*), 2) AS avg_order_value
FROM orders
WHERE order_date >= '2024-01-01' AND order_date < '2024-04-01';
```
**Expected Result:**

| avg_order_value |
|-----------------|
| 6000            |

---

## Summary Table

| Metric                    | Value   |
|---------------------------|---------|
| Total sales for March     | 27,000  |
| Top-spending customer     | Alice   |
| Top customer total spent  | 20,000  |
| Average order value       | 6,000   | 