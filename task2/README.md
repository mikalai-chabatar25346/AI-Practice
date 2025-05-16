# API Testing: Product Data Validation

This project implements automated tests to validate product data from the Fake Store API (<https://fakestoreapi.com/products>).

## Setup

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run the test suite:

```bash
pytest tests/test_products.py -v
```

Generate HTML report:

```bash
pytest tests/test_products.py --html=report.html
```

## Test Cases

1. Server Response Code (200)
2. Product Title Validation
3. Price Validation
4. Rating Validation

## Project Structure

``` sh
task2/
├── tests/
│   └── test_products.py
├── requirements.txt
└── README.md
```
