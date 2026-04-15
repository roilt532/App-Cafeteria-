#!/usr/bin/env python3
import requests
import sys
from datetime import datetime

class PioBiteAPITester:
    def __init__(self, base_url="https://5a51f588-5b80-4e9a-b073-187bf28fd15a.preview.emergentagent.com"):
        self.base_url = base_url
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    print(f"   Response: {response_data}")
                    return True, response_data
                except:
                    return True, {}
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text}")
                self.failed_tests.append(f"{name}: Expected {expected_status}, got {response.status_code}")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            self.failed_tests.append(f"{name}: {str(e)}")
            return False, {}

    def test_health(self):
        """Test health endpoint"""
        return self.run_test("Health Check", "GET", "api/health", 200)

    def test_products(self):
        """Test products endpoint"""
        success, data = self.run_test("Get All Products", "GET", "api/products", 200)
        if success and isinstance(data, list) and len(data) > 0:
            print(f"   Found {len(data)} products")
            return True
        return False

    def test_products_by_category(self):
        """Test products by category"""
        categories = ["bocadillos", "bolleria", "ensaladas", "bebidas_calientes", "bebidas_frias"]
        for category in categories:
            success, data = self.run_test(f"Get Products - {category}", "GET", f"api/products?category={category}", 200)
            if success and isinstance(data, list):
                print(f"   Found {len(data)} products in {category}")

    def test_categories(self):
        """Test categories endpoint"""
        success, data = self.run_test("Get Categories", "GET", "api/categories", 200)
        if success and isinstance(data, list) and len(data) > 0:
            print(f"   Found {len(data)} categories")
            return True
        return False

    def test_timeslots(self):
        """Test timeslots endpoint"""
        success, data = self.run_test("Get Time Slots", "GET", "api/timeslots", 200)
        if success and isinstance(data, list) and len(data) > 0:
            print(f"   Found {len(data)} time slots")
            return True
        return False

    def test_orders(self):
        """Test orders endpoint"""
        success, data = self.run_test("Get Orders", "GET", "api/orders", 200)
        if success and isinstance(data, list):
            print(f"   Found {len(data)} orders")
            return True
        return False

    def test_admin_orders(self):
        """Test admin orders endpoint"""
        success, data = self.run_test("Get Admin Orders", "GET", "api/admin/orders", 200)
        if success and isinstance(data, list):
            print(f"   Found {len(data)} admin orders")
            return True
        return False

    def test_create_order(self):
        """Test order creation"""
        order_data = {
            "items": [
                {"name": "Bocadillo de Jamón Serrano", "qty": 1, "price": 3.50},
                {"name": "Café con Leche", "qty": 1, "price": 1.50}
            ],
            "total": 5.00,
            "timeSlot": "10:00 - 10:30"
        }
        success, data = self.run_test("Create Order", "POST", "api/orders", 200, order_data)
        if success and 'code' in data and 'id' in data:
            print(f"   Order created with code: {data.get('code')}")
            return True
        return False

def main():
    print("🚀 Starting PíoBite API Tests...")
    print("=" * 50)
    
    tester = PioBiteAPITester()
    
    # Run all tests
    tester.test_health()
    tester.test_products()
    tester.test_products_by_category()
    tester.test_categories()
    tester.test_timeslots()
    tester.test_orders()
    tester.test_admin_orders()
    tester.test_create_order()
    
    # Print results
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {tester.tests_passed}/{tester.tests_run} passed")
    
    if tester.failed_tests:
        print("\n❌ Failed Tests:")
        for test in tester.failed_tests:
            print(f"   - {test}")
    
    success_rate = (tester.tests_passed / tester.tests_run) * 100 if tester.tests_run > 0 else 0
    print(f"📈 Success Rate: {success_rate:.1f}%")
    
    return 0 if tester.tests_passed == tester.tests_run else 1

if __name__ == "__main__":
    sys.exit(main())