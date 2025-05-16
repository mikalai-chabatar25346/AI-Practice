import sqlite3
import unittest
from datetime import datetime

class TestOrderQueries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Create in-memory database
        cls.conn = sqlite3.connect(':memory:')
        cls.cursor = cls.conn.cursor()
        
        # Read and execute SQL file
        with open('queries.sql', 'r') as sql_file:
            sql_script = sql_file.read()
            cls.cursor.executescript(sql_script)
        cls.conn.commit()

    def test_total_sales_march_2024(self):
        self.cursor.execute("""
            SELECT SUM(amount) as total_sales
            FROM orders
            WHERE strftime('%Y-%m', order_date) = '2024-03'
        """)
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 27000, "Total sales for March 2024 should be 27,000")

    def test_top_customer(self):
        self.cursor.execute("""
            SELECT 
                customer,
                SUM(amount) as total_spent
            FROM orders
            GROUP BY customer
            ORDER BY total_spent DESC
            LIMIT 1
        """)
        result = self.cursor.fetchone()
        self.assertEqual(result[0], 'Alice', "Top customer should be Alice")
        self.assertEqual(result[1], 20000, "Alice's total spent should be 20,000")

    def test_average_order_value(self):
        self.cursor.execute("""
            SELECT AVG(amount) as average_order_value
            FROM orders
        """)
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 5400, "Average order value should be 5,400")

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

if __name__ == '__main__':
    unittest.main() 