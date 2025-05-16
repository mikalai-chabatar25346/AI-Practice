import pytest
import requests
import json
import logging
import sys
from datetime import datetime
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('test_results.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class TestProductAPI:
    """Test suite for Fake Store API product validation"""
    
    @pytest.fixture(autouse=True)
    def setup_logging(self):
        """Setup logging for each test"""
        logger.info("=" * 50)
        logger.info("Starting new test")
        yield
        logger.info("Test completed")
        logger.info("=" * 50)
    
    @pytest.fixture(scope="class")
    def api_url(self) -> str:
        return "https://fakestoreapi.com/products"
    
    @pytest.fixture(scope="class")
    def products(self, api_url: str) -> List[Dict[str, Any]]:
        """Fetch all products from the API"""
        logger.info(f"Fetching products from {api_url}")
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            products = response.json()
            logger.info(f"Successfully fetched {len(products)} products")
            return products
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch products: {str(e)}")
            raise
    
    def test_server_response(self, api_url: str):
        """Test 1: Verify server response code"""
        logger.info("Testing server response")
        try:
            response = requests.get(api_url)
            response.raise_for_status()
            logger.info(f"Server response successful: {response.status_code}")
            assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
        except requests.exceptions.RequestException as e:
            logger.error(f"Server response failed: {str(e)}")
            raise
    
    def test_product_titles(self, products: List[Dict[str, Any]]):
        """Test 2: Validate product titles"""
        logger.info("Testing product titles")
        defective_products = []
        
        for product in products:
            if not product.get('title'):
                defective_products.append({
                    'id': product.get('id'),
                    'title': product.get('title'),
                    'defect': 'Empty title',
                    'link': f"https://fakestoreapi.com/products/{product.get('id')}"
                })
        
        if defective_products:
            logger.warning(f"Found {len(defective_products)} products with empty titles")
            for product in defective_products:
                logger.warning(f"Product ID {product['id']}: {product['defect']} - Link: {product['link']}")
        else:
            logger.info("All product titles are valid")
        
        assert len(defective_products) == 0, f"Found products with empty titles: {defective_products}"
    
    def test_product_prices(self, products: List[Dict[str, Any]]):
        """Test 3: Validate product prices"""
        logger.info("Testing product prices")
        defective_products = []
        
        for product in products:
            price = product.get('price')
            if price is None or price < 0:
                defective_products.append({
                    'id': product.get('id'),
                    'title': product.get('title'),
                    'price': price,
                    'defect': 'Invalid price',
                    'link': f"https://fakestoreapi.com/products/{product.get('id')}"
                })
        
        if defective_products:
            logger.warning(f"Found {len(defective_products)} products with invalid prices")
            for product in defective_products:
                logger.warning(f"Product ID {product['id']}: {product['defect']} - Price: {product['price']} - Link: {product['link']}")
        else:
            logger.info("All product prices are valid")
        
        assert len(defective_products) == 0, f"Found products with invalid prices: {defective_products}"
    
    def test_product_ratings(self, products: List[Dict[str, Any]]):
        """Test 4: Validate product ratings"""
        logger.info("Testing product ratings")
        defective_products = []
        
        for product in products:
            rating = product.get('rating', {})
            rate = rating.get('rate')
            
            if rate is None or rate > 5:
                defective_products.append({
                    'id': product.get('id'),
                    'title': product.get('title'),
                    'rating': rate,
                    'defect': 'Invalid rating',
                    'link': f"https://fakestoreapi.com/products/{product.get('id')}"
                })
        
        if defective_products:
            logger.warning(f"Found {len(defective_products)} products with invalid ratings")
            for product in defective_products:
                logger.warning(f"Product ID {product['id']}: {product['defect']} - Rating: {product['rating']} - Link: {product['link']}")
        else:
            logger.info("All product ratings are valid")
        
        assert len(defective_products) == 0, f"Found products with invalid ratings: {defective_products}"
    
    def test_generate_defect_report(self, products: List[Dict[str, Any]]):
        """Generate comprehensive defect report"""
        logger.info("Generating defect report")
        defects = []
        
        for product in products:
            product_defects = []
            
            # Check title
            if not product.get('title'):
                product_defects.append('Empty title')
            
            # Check price
            price = product.get('price')
            if price is None or price < 0:
                product_defects.append('Invalid price')
            
            # Check rating
            rating = product.get('rating', {})
            rate = rating.get('rate')
            if rate is None or rate > 5:
                product_defects.append('Invalid rating')
            
            if product_defects:
                defects.append({
                    'product_id': product.get('id'),
                    'title': product.get('title'),
                    'defects': product_defects,
                    'link': f"https://fakestoreapi.com/products/{product.get('id')}"
                })
        
        # Generate report
        report = {
            'test_summary': {
                'total_products': len(products),
                'defective_products': len(defects),
                'test_timestamp': datetime.now().isoformat()
            },
            'defects': defects
        }
        
        # Save report to file
        with open('defect_report.json', 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Defect report generated: {len(defects)} defective products found")
        if defects:
            logger.warning("Defective products found:")
            for defect in defects:
                logger.warning(f"Product ID {defect['product_id']}: {defect['defects']} - Link: {defect['link']}")
        
        assert len(defects) == 0, f"Found {len(defects)} defective products" 