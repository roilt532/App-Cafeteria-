#!/usr/bin/env python3
import requests
import sys
from datetime import datetime

class PioBiteAPITester:
    def __init__(self, base_url="https://baroja-cafe-order.preview.emergentagent.com"):
        self.base_url = base_url
        self.token = None
        self.admin_token = None
        self.tests_run = 0
        self.tests_passed = 0
        self.failed_tests = []

    def run_test(self, name, method, endpoint, expected_status, data=None, auth_token=None):
        """Run a single API test"""
        url = f"{self.base_url}/{endpoint}"
        headers = {'Content-Type': 'application/json'}
        if auth_token:
            headers['Authorization'] = f'Bearer {auth_token}'

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=headers, timeout=10)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=headers, timeout=10)
            elif method == 'PATCH':
                response = requests.patch(url, json=data, headers=headers, timeout=10)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    response_data = response.json()
                    if len(str(response_data)) > 200:
                        print(f"   Response: [Large response - {len(str(response_data))} chars]")
                    else:
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
        success, data = self.run_test("Health Check", "GET", "api/health", 200)
        if success and data.get("version") == "2.0.0":
            print(f"   Version: {data.get('version')}")
            return True
        return False

    def test_auth_register(self):
        """Test user registration"""
        test_user = f"test_{datetime.now().strftime('%H%M%S')}@piobaroja.es"
        user_data = {
            "name": "Test User",
            "email": test_user,
            "password": "test123",
            "role": "client"
        }
        success, data = self.run_test("User Registration", "POST", "api/auth/register", 200, user_data)
        if success and 'access' in data:
            self.token = data['access']
            print(f"   User registered: {data.get('email')}")
            return True
        return False

    def test_auth_login_admin(self):
        """Test admin login"""
        login_data = {
            "email": "admin@piobite.es",
            "password": "admin123"
        }
        success, data = self.run_test("Admin Login", "POST", "api/auth/login", 200, login_data)
        if success and 'access' in data and data.get('role') == 'admin':
            self.admin_token = data['access']
            print(f"   Admin logged in: {data.get('email')}")
            return True
        return False

    def test_auth_me(self):
        """Test get current user"""
        if not self.token:
            print("❌ No token available for auth/me test")
            return False
        success, data = self.run_test("Get Current User", "GET", "api/auth/me", 200, auth_token=self.token)
        if success and 'email' in data:
            print(f"   Current user: {data.get('email')}")
            return True
        return False

    def test_products(self):
        """Test products endpoint"""
        success, data = self.run_test("Get All Products", "GET", "api/productos", 200)
        if success and isinstance(data, list) and len(data) == 12:
            print(f"   Found {len(data)} products")
            return True
        return False

    def test_products_by_category(self):
        """Test products by category"""
        success, data = self.run_test("Get Bocadillos", "GET", "api/productos?categoria=bocadillos", 200)
        if success and isinstance(data, list):
            print(f"   Found {len(data)} bocadillos")
            return True
        return False

    def test_categories(self):
        """Test categories endpoint"""
        success, data = self.run_test("Get Categories", "GET", "api/categorias", 200)
        if success and isinstance(data, list) and len(data) == 5:
            print(f"   Found {len(data)} categories")
            return True
        return False

    def test_timeslots(self):
        """Test timeslots endpoint"""
        success, data = self.run_test("Get Time Slots", "GET", "api/franjas-horarias", 200)
        if success and isinstance(data, list) and len(data) > 0:
            print(f"   Found {len(data)} time slots")
            return True
        return False

    def test_create_order(self):
        """Test order creation"""
        if not self.token:
            print("❌ No token available for order creation")
            return False
        
        # First get a product ID
        success, products = self.run_test("Get Products for Order", "GET", "api/productos", 200)
        if not success or not products:
            return False
            
        product_id = products[0]['id']
        order_data = {
            "items": [
                {"producto_id": product_id, "cantidad": 1}
            ]
        }
        success, data = self.run_test("Create Order", "POST", "api/pedidos", 200, order_data, auth_token=self.token)
        if success and 'codigo' in data:
            print(f"   Order created with code: {data.get('codigo')}")
            return True
        return False

    def test_admin_orders(self):
        """Test admin orders endpoint"""
        if not self.admin_token:
            print("❌ No admin token available")
            return False
        success, data = self.run_test("Get Admin Orders", "GET", "api/pedidos/admin", 200, auth_token=self.admin_token)
        if success and isinstance(data, list):
            print(f"   Found {len(data)} admin orders")
            return True
        return False

    def test_inventory(self):
        """Test inventory endpoint"""
        if not self.admin_token:
            print("❌ No admin token available")
            return False
        success, data = self.run_test("Get Inventory", "GET", "api/inventario", 200, auth_token=self.admin_token)
        if success and isinstance(data, list):
            print(f"   Found {len(data)} inventory items")
            return True
        return False

    def test_stats(self):
        """Test statistics endpoints"""
        if not self.admin_token:
            print("❌ No admin token available")
            return False
        
        success1, data1 = self.run_test("Get Stats Summary", "GET", "api/estadisticas/resumen", 200, auth_token=self.admin_token)
        success2, data2 = self.run_test("Get Top Products", "GET", "api/estadisticas/productos-top", 200, auth_token=self.admin_token)
        
        if success1 and 'pedidos_totales' in data1 and success2 and isinstance(data2, list):
            print(f"   Stats: {data1.get('pedidos_totales')} total orders")
            print(f"   Top products: {len(data2)} items")
            return True
        return False

    def test_payment_simulation(self):
        """Test payment simulation"""
        if not self.token:
            print("❌ No token available for payment test")
            return False
        
        # Create an order first
        success, products = self.run_test("Get Products for Payment", "GET", "api/productos", 200)
        if not success or not products:
            return False
            
        product_id = products[0]['id']
        order_data = {
            "items": [{"producto_id": product_id, "cantidad": 1}]
        }
        success, order = self.run_test("Create Order for Payment", "POST", "api/pedidos", 200, order_data, auth_token=self.token)
        if not success or 'id' not in order:
            return False
        
        # Test payment initiation
        payment_data = {"pedido_id": order['id']}
        success, data = self.run_test("Initiate Payment", "POST", "api/pagos/iniciar", 200, payment_data, auth_token=self.token)
        if success and data.get('simulado') == True:
            print(f"   Payment simulation initialized")
            return True
        return False

def main():
    print("🚀 Starting PíoBite API Tests (Real MongoDB Implementation)...")
    print("=" * 60)
    
    tester = PioBiteAPITester()
    
    # Run all tests in order
    print("\n📋 BASIC ENDPOINTS")
    tester.test_health()
    
    print("\n🔐 AUTHENTICATION")
    tester.test_auth_register()
    tester.test_auth_login_admin()
    tester.test_auth_me()
    
    print("\n🍽️ PRODUCTS & CATEGORIES")
    tester.test_products()
    tester.test_products_by_category()
    tester.test_categories()
    tester.test_timeslots()
    
    print("\n📦 ORDERS")
    tester.test_create_order()
    tester.test_admin_orders()
    
    print("\n👨‍💼 ADMIN FEATURES")
    tester.test_inventory()
    tester.test_stats()
    
    print("\n💳 PAYMENT SIMULATION")
    tester.test_payment_simulation()
    
    # Print results
    print("\n" + "=" * 60)
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