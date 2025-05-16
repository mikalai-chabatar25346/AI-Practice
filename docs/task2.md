# API Testing: Identifying Defects in Product Data

## Overview

This document outlines the automated tests implemented to validate product data from the Fake Store API (<https://fakestoreapi.com/products>). The tests are designed to identify defects and anomalies in the product data.

## Test Implementation

```python
import requests
import json
from typing import List, Dict

def test_product_data():
    # API endpoint
    url = "https://fakestoreapi.com/products"
    
    # Make GET request
    response = requests.get(url)
    
    # Test 1: Verify server response code
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Parse JSON response
    products = response.json()
    
    # Initialize list to store defective products
    defective_products = []
    
    # Test each product
    for product in products:
        defects = []
        
        # Test 2: Check if title is empty
        if not product.get('title'):
            defects.append("Empty title")
            
        # Test 3: Check if price is negative
        if product.get('price', 0) < 0:
            defects.append("Negative price")
            
        # Test 4: Check if rating.rate exceeds 5
        rating = product.get('rating', {})
        if rating.get('rate', 0) > 5:
            defects.append("Rating exceeds 5")
            
        # If any defects found, add to defective products list
        if defects:
            defective_products.append({
                'id': product.get('id'),
                'title': product.get('title'),
                'defects': defects
            })
    
    return defective_products

# Run tests and print results
if __name__ == "__main__":
    try:
        defective_products = test_product_data()
        
        print("\nDefective Products Found:")
        print("=========================")
        for product in defective_products:
            print(f"\nProduct ID: {product['id']}")
            print(f"Title: {product['title']}")
            print("Defects:")
            for defect in product['defects']:
                print(f"- {defect}")
                
    except Exception as e:
        print(f"Error during testing: {str(e)}")
```

## Test Cases

1. **Server Response Code**
   - Expected: 200
   - Purpose: Verify that the API endpoint is accessible and responding correctly

2. **Product Title Validation**
   - Check: Title must not be empty
   - Purpose: Ensure all products have valid names

3. **Price Validation**
   - Check: Price must not be negative
   - Purpose: Ensure all products have valid pricing

4. **Rating Validation**
   - Check: Rating.rate must not exceed 5
   - Purpose: Ensure ratings are within the valid range (0-5)

## How to Run the Tests

1. Ensure you have Python installed on your system
2. Install the required package:

   ```bash
   pip install requests
   ```

3. Save the test code in a Python file (e.g., `test_products.py`)
4. Run the script:

   ```bash
   python test_products.py
   ```

## Expected Output

The script will output a list of products that contain defects, including:

- Product ID
- Product Title
- List of specific defects found

## Notes

- The tests are designed to be non-destructive and only read data from the API
- The script handles potential API errors gracefully
- Results are presented in a clear, readable format
- The test suite can be extended to include additional validation rules as needed
