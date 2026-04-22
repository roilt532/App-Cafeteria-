# PíoBite - Cafetería Instituto Pío Baroja - PRD

## Problem Statement
Aplicación móvil de pedidos para la cafetería del Instituto Pío Baroja con API REST completa.

## Architecture
- **Frontend**: React 18 + Tailwind CSS + React Router v6 + react-qr-code
- **Backend**: FastAPI (Python) + MongoDB (motor) + JWT Auth (bcrypt + PyJWT)
- **Database**: MongoDB con colecciones: users, products, categories, orders, timeslots
- **Responsive**: Mobile-first, tablet y desktop

## What's Been Implemented

### Fase 1 - Prototipo (April 15, 2025)
- [x] 11 pantallas navegables con diseño responsive
- [x] Catálogo de 12 productos, 6 categorías
- [x] Sistema de traducciones ES/EN completo

### Fase 2 - API REST Completa (April 22, 2025)
- [x] Backend real con MongoDB (no más datos mock)
- [x] JWT Authentication (register, login, logout, refresh, me)
- [x] Admin seeding automático al inicio
- [x] CRUD completo de productos con stock
- [x] Gestión de pedidos con transiciones de estado validadas
- [x] Simulación de pasarela de pago Redsys
- [x] Panel de Inventario (gestión de stock, disponibilidad)
- [x] Panel de Estadísticas (ventas, productos top, estados)
- [x] Gestión de errores estructurada (códigos, mensajes)
- [x] Verificación de pedidos por código
- [x] Franjas horarias con capacidad/ocupación

### Documentación Generada
- [x] prototipo.html - Presentación visual de todas las pantallas
- [x] diseno-api-rest.html - Documento técnico de diseño API REST
- [x] README.md - Documentación del proyecto

## Testing Status
- Backend: 100% pass
- Frontend: 100% pass

## Prioritized Backlog
### P0
- Google OAuth real (SSO)
- Integración Redsys real
- Push notifications

### P1
- QR code scanning en admin
- PWA support
- Image upload para productos

### P2
- Real-time order tracking
- Advanced analytics
- Export reports
