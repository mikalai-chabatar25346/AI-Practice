# SQL Queries Implementation

This implementation provides SQL queries for analyzing order data, including total sales calculations, customer spending analysis, and average order value computations.

## Files

- `queries.sql`: Contains the database schema, sample data, and SQL queries
- `test_queries.py`: Python test suite to verify query results

## Database Schema

The `orders` table has the following structure:
- `id` (INTEGER PRIMARY KEY)
- `customer` (TEXT)
- `amount` (REAL)
- `order_date` (DATE)

## Queries

1. **Total Sales for March 2024**
   - Calculates the sum of all order amounts for March 2024
   - Expected result: 27,000

2. **Top Customer Analysis**
   - Identifies the customer with the highest total spending
   - Expected result: Alice with 20,000

3. **Average Order Value**
   - Calculates the average amount per order
   - Expected result: 5,400

## Running Tests

To run the tests, execute:
```bash
python test_queries.py
```

## Test Cases

The test suite includes:
- Total sales calculation verification
- Top customer identification
- Average order value computation
- Edge cases handling

## Performance Considerations

- The implementation uses SQLite for simplicity and testing
- For production use, consider:
  - Adding indexes on `order_date` and `customer` columns
  - Implementing query optimization for larger datasets
  - Using a more robust database system for production environments 