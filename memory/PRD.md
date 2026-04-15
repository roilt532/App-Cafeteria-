# PíoBite - Cafetería Instituto Pío Baroja - PRD

## Problem Statement
Aplicación móvil de pedidos para la cafetería del Instituto Pío Baroja. Fase 1: Prototipo navegable con todas las pantallas y flujos de usuario.

## Architecture
- **Frontend**: React 18 + Tailwind CSS + React Router v6 + react-qr-code
- **Backend**: FastAPI (Python) - API minimal con datos mock
- **Database**: MongoDB (configurado, no usado en prototipo)
- **Responsive**: Mobile-first, adaptado a tablet y desktop

## User Personas
1. **Alumno/Cliente**: Estudiante del instituto que pide comida
2. **Admin (Cafetería)**: Personal del servicio que gestiona pedidos

## Core Requirements (Static)
- Login/Register con selección de rol
- Catálogo de productos con categorías y búsqueda
- Carrito de compra con gestión de cantidades
- Selección de franja horaria de recogida
- Confirmación de pedido con código QR
- Historial de pedidos
- Favoritos
- Perfil con toggle idioma ES/EN
- Panel Admin con gestión de pedidos y verificación de código
- Navegación responsiva: Bottom Nav (móvil) / Sidebar (tablet/desktop)

## What's Been Implemented (April 15, 2025)
- [x] Pantalla de bienvenida con branding PíoBite
- [x] Login con toggle de rol (Cliente/Admin) + botón Google
- [x] Registro con selección visual de rol
- [x] Catálogo con 12 productos, 6 categorías, búsqueda, favoritos
- [x] Carrito con controles de cantidad (+/-), eliminar, total
- [x] Selección de franja horaria (8 slots)
- [x] Confirmación de pedido con QR code real (react-qr-code)
- [x] Historial con 3 pedidos mock y estados
- [x] Pantalla de favoritos
- [x] Perfil con toggle ES/EN, info de usuario, logout
- [x] Panel Admin con tabs de estado, verificación de código, acciones
- [x] Bottom Nav (móvil) y Sidebar (tablet/desktop)
- [x] Sistema completo de traducciones ES/EN

## Testing Status
- Backend: 100% pass
- Frontend: 95% pass (minor LOW priority issues fixed)

## Prioritized Backlog
### P0 (Next Phase)
- Real authentication (JWT + Google OAuth)
- Backend API connected to MongoDB
- Real CRUD for products, orders, users

### P1
- Push notifications
- Payment gateway integration
- QR code scanning on admin side
- Image upload for products

### P2
- Order tracking in real-time
- Advanced admin analytics
- Multi-language expansion
- PWA support for offline mode

## Products Catalog
12 products across 6 categories:
- Bocadillos: Jamón Serrano (3.50€), Tortilla (3.00€), Sandwich Vegetal (3.20€), Tostada Tomate (1.80€)
- Bollería: Croissant Mixto (2.50€), Napolitana Chocolate (1.80€)
- Ensaladas: César (4.50€)
- Bebidas Calientes: Café con Leche (1.50€), Café Solo (1.20€)
- Bebidas Frías: Zumo Naranja (2.00€), Agua Mineral (1.00€), Batido Chocolate (2.50€)
