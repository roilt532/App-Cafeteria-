from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
import uuid
from datetime import datetime, timezone

load_dotenv()

app = FastAPI(title="PíoBite API - Cafetería Pío Baroja")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PRODUCTS = [
    {"id": "p1", "name": "Bocadillo de Jamón Serrano", "nameEn": "Serrano Ham Sandwich", "price": 3.50, "category": "bocadillos", "description": "Pan crujiente con jamón serrano de calidad", "descriptionEn": "Crusty bread with quality Serrano ham", "image": "https://images.unsplash.com/photo-1544723295-b451ddfb68ae?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjY2NjV8MHwxfHNlYXJjaHwyfHx0YXN0eSUyMGFydGlzYW4lMjBzYW5kd2ljaCUyMGJ1cmdlcnxlbnwwfHx8fDE3NzYyNDg4Mzl8MA&ixlib=rb-4.1.0&q=85", "healthy": False, "popular": True},
    {"id": "p2", "name": "Bocadillo de Tortilla", "nameEn": "Spanish Omelette Sandwich", "price": 3.00, "category": "bocadillos", "description": "Tortilla española casera en pan de barra", "descriptionEn": "Homemade Spanish omelette in baguette", "image": "https://images.unsplash.com/photo-1762335753199-6d4af2053b34?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjY2NjV8MHwxfHNlYXJjaHwxfHx0YXN0eSUyMGFydGlzYW4lMjBzYW5kd2ljaCUyMGJ1cmdlcnxlbnwwfHx8fDE3NzYyNDg4Mzl8MA&ixlib=rb-4.1.0&q=85", "healthy": False, "popular": True},
    {"id": "p3", "name": "Croissant Mixto", "nameEn": "Ham & Cheese Croissant", "price": 2.50, "category": "bolleria", "description": "Croissant relleno de jamón york y queso", "descriptionEn": "Croissant filled with ham and cheese", "image": "https://images.pexels.com/photos/30853716/pexels-photo-30853716.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "healthy": False, "popular": True},
    {"id": "p4", "name": "Napolitana de Chocolate", "nameEn": "Chocolate Pastry", "price": 1.80, "category": "bolleria", "description": "Napolitana crujiente con chocolate fundido", "descriptionEn": "Crispy pastry with melted chocolate", "image": "https://images.unsplash.com/photo-1737700088850-d0b53f9d39ec?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDJ8MHwxfHNlYXJjaHwzfHxjcm9pc3NhbnQlMjBwYXN0cnklMjBiYWtlcnl8ZW58MHx8fHwxNzc2MjQ4OTI2fDA&ixlib=rb-4.1.0&q=85", "healthy": False, "popular": False},
    {"id": "p5", "name": "Ensalada César", "nameEn": "Caesar Salad", "price": 4.50, "category": "ensaladas", "description": "Lechuga, pollo, crutones, parmesano y salsa César", "descriptionEn": "Lettuce, chicken, croutons, parmesan and Caesar dressing", "image": "https://images.unsplash.com/photo-1622637103261-ae624e188bd0?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjY2NzF8MHwxfHNlYXJjaHw0fHxmcmVzaCUyMGhlYWx0aHklMjBzYWxhZCUyMGJvd2x8ZW58MHx8fHwxNzc2MjQ4ODM5fDA&ixlib=rb-4.1.0&q=85", "healthy": True, "popular": False},
    {"id": "p6", "name": "Sandwich Vegetal", "nameEn": "Veggie Sandwich", "price": 3.20, "category": "bocadillos", "description": "Pan integral con lechuga, tomate, huevo y atún", "descriptionEn": "Whole wheat bread with lettuce, tomato, egg and tuna", "image": "https://images.unsplash.com/photo-1762335753199-6d4af2053b34?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjY2NjV8MHwxfHNlYXJjaHwxfHx0YXN0eSUyMGFydGlzYW4lMjBzYW5kd2ljaCUyMGJ1cmdlcnxlbnwwfHx8fDE3NzYyNDg4Mzl8MA&ixlib=rb-4.1.0&q=85", "healthy": True, "popular": False},
    {"id": "p7", "name": "Café con Leche", "nameEn": "Latte", "price": 1.50, "category": "bebidas_calientes", "description": "Café espresso con leche caliente", "descriptionEn": "Espresso with hot milk", "image": "https://images.unsplash.com/photo-1647972488473-ca3796499272?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Njl8MHwxfHNlYXJjaHwzfHxjb2ZmZWUlMjBwYXBlciUyMGN1cCUyMGNhZmV8ZW58MHx8fHwxNzc2MjQ4ODU3fDA&ixlib=rb-4.1.0&q=85", "healthy": False, "popular": True},
    {"id": "p8", "name": "Café Solo", "nameEn": "Espresso", "price": 1.20, "category": "bebidas_calientes", "description": "Café espresso intenso", "descriptionEn": "Strong espresso coffee", "image": "https://images.unsplash.com/photo-1647972488473-ca3796499272?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NTY2Njl8MHwxfHNlYXJjaHwzfHxjb2ZmZWUlMjBwYXBlciUyMGN1cCUyMGNhZmV8ZW58MHx8fHwxNzc2MjQ4ODU3fDA&ixlib=rb-4.1.0&q=85", "healthy": False, "popular": False},
    {"id": "p9", "name": "Zumo de Naranja Natural", "nameEn": "Fresh Orange Juice", "price": 2.00, "category": "bebidas_frias", "description": "Zumo de naranja recién exprimido", "descriptionEn": "Freshly squeezed orange juice", "image": "https://images.unsplash.com/photo-1759269106039-ffbe70b406fb?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4NjA1NzB8MHwxfHNlYXJjaHwxfHxmcmVzaCUyMG9yYW5nZSUyMGp1aWNlJTIwZ2xhc3MlMjBjYWZlfGVufDB8fHx8MTc3NjI0ODkxOHww&ixlib=rb-4.1.0&q=85", "healthy": True, "popular": True},
    {"id": "p10", "name": "Agua Mineral", "nameEn": "Mineral Water", "price": 1.00, "category": "bebidas_frias", "description": "Botella de agua mineral 500ml", "descriptionEn": "500ml mineral water bottle", "image": "https://images.pexels.com/photos/1540235/pexels-photo-1540235.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940", "healthy": True, "popular": False},
    {"id": "p11", "name": "Batido de Chocolate", "nameEn": "Chocolate Milkshake", "price": 2.50, "category": "bebidas_frias", "description": "Batido cremoso de chocolate con nata", "descriptionEn": "Creamy chocolate milkshake with cream", "image": "https://images.unsplash.com/photo-1648071597664-ffabc1e1c13b?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2MzR8MHwxfHNlYXJjaHwxfHxjaG9jb2xhdGUlMjBtaWxrc2hha2UlMjBzbW9vdGhpZXxlbnwwfHx8fDE3NzYyNDg5Mzh8MA&ixlib=rb-4.1.0&q=85", "healthy": False, "popular": True},
    {"id": "p12", "name": "Tostada con Tomate", "nameEn": "Toast with Tomato", "price": 1.80, "category": "bocadillos", "description": "Tostada con aceite de oliva y tomate rallado", "descriptionEn": "Toast with olive oil and grated tomato", "image": "https://images.unsplash.com/photo-1751151856149-5ebf1d21586a?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDQ2NDJ8MHwxfHNlYXJjaHwxfHxjcm9pc3NhbnQlMjBwYXN0cnklMjBiYWtlcnl8ZW58MHx8fHwxNzc2MjQ4OTI2fDA&ixlib=rb-4.1.0&q=85", "healthy": True, "popular": False},
]

CATEGORIES = [
    {"id": "all", "name": "Todos", "nameEn": "All", "icon": "grid"},
    {"id": "bocadillos", "name": "Bocadillos", "nameEn": "Sandwiches", "icon": "sandwich"},
    {"id": "bolleria", "name": "Bollería", "nameEn": "Pastries", "icon": "croissant"},
    {"id": "ensaladas", "name": "Ensaladas", "nameEn": "Salads", "icon": "salad"},
    {"id": "bebidas_calientes", "name": "Bebidas Calientes", "nameEn": "Hot Drinks", "icon": "coffee"},
    {"id": "bebidas_frias", "name": "Bebidas Frías", "nameEn": "Cold Drinks", "icon": "cup-soda"},
]

TIME_SLOTS = [
    {"id": "ts1", "time": "09:30 - 10:00", "available": True},
    {"id": "ts2", "time": "10:00 - 10:30", "available": True},
    {"id": "ts3", "time": "10:30 - 11:00", "available": True},
    {"id": "ts4", "time": "11:00 - 11:30", "available": True},
    {"id": "ts5", "time": "11:30 - 12:00", "available": False},
    {"id": "ts6", "time": "12:00 - 12:30", "available": True},
    {"id": "ts7", "time": "12:30 - 13:00", "available": True},
    {"id": "ts8", "time": "13:00 - 13:30", "available": True},
]

MOCK_ORDERS = [
    {"id": "ORD-PB2401", "items": [{"name": "Bocadillo de Jamón Serrano", "qty": 1, "price": 3.50}, {"name": "Café con Leche", "qty": 1, "price": 1.50}], "total": 5.00, "status": "entregado", "statusEn": "delivered", "date": "2025-04-14", "timeSlot": "10:00 - 10:30", "code": "PB2401"},
    {"id": "ORD-PB2402", "items": [{"name": "Ensalada César", "qty": 1, "price": 4.50}, {"name": "Zumo de Naranja", "qty": 1, "price": 2.00}], "total": 6.50, "status": "preparando", "statusEn": "preparing", "date": "2025-04-15", "timeSlot": "11:00 - 11:30", "code": "PB2402"},
    {"id": "ORD-PB2403", "items": [{"name": "Croissant Mixto", "qty": 2, "price": 2.50}], "total": 5.00, "status": "pendiente", "statusEn": "pending", "date": "2025-04-15", "timeSlot": "09:30 - 10:00", "code": "PB2403"},
]

ADMIN_ORDERS = [
    {"id": "ORD-PB2402", "customer": "María García", "items": [{"name": "Ensalada César", "qty": 1}, {"name": "Zumo de Naranja", "qty": 1}], "total": 6.50, "status": "preparando", "timeSlot": "11:00 - 11:30", "code": "PB2402", "date": "2025-04-15"},
    {"id": "ORD-PB2403", "customer": "Carlos López", "items": [{"name": "Croissant Mixto", "qty": 2}], "total": 5.00, "status": "pendiente", "timeSlot": "09:30 - 10:00", "code": "PB2403", "date": "2025-04-15"},
    {"id": "ORD-PB2404", "customer": "Ana Martínez", "items": [{"name": "Café con Leche", "qty": 1}, {"name": "Napolitana de Chocolate", "qty": 1}], "total": 3.30, "status": "listo", "timeSlot": "10:30 - 11:00", "code": "PB2404", "date": "2025-04-15"},
    {"id": "ORD-PB2405", "customer": "Pedro Sánchez", "items": [{"name": "Bocadillo de Tortilla", "qty": 1}, {"name": "Agua Mineral", "qty": 1}], "total": 4.00, "status": "entregado", "timeSlot": "10:00 - 10:30", "code": "PB2405", "date": "2025-04-15"},
]


@app.get("/api/health")
async def health_check():
    return {"status": "ok", "app": "PíoBite API", "version": "1.0.0"}


@app.get("/api/products")
async def get_products(category: str = None):
    if category and category != "all":
        return [p for p in PRODUCTS if p["category"] == category]
    return PRODUCTS


@app.get("/api/categories")
async def get_categories():
    return CATEGORIES


@app.get("/api/timeslots")
async def get_timeslots():
    return TIME_SLOTS


@app.get("/api/orders")
async def get_orders():
    return MOCK_ORDERS


@app.get("/api/admin/orders")
async def get_admin_orders():
    return ADMIN_ORDERS


@app.post("/api/orders")
async def create_order(order: dict):
    order_code = f"PB{uuid.uuid4().hex[:4].upper()}"
    return {
        "id": f"ORD-{order_code}",
        "code": order_code,
        "status": "pendiente",
        "date": datetime.now(timezone.utc).isoformat(),
        **order,
    }
