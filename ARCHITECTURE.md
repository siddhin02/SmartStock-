# System Architecture

## SmartStock – Inventory & Billing Software

This document describes the overall system architecture, technology stack, folder structure, data flow, and key design decisions for the SmartStock application.

---

## 1. High-Level Architecture

SmartStock follows a traditional server-rendered MVC web architecture using Python Flask.

```
User (Web Browser)
        ↓ HTTP/HTTPS
Flask Frontend (Jinja2 Templates + Bootstrap 5)
        ↓
Flask Backend (Blueprints / Routes / Services)
        ↓
SQLAlchemy ORM
        ↓
MySQL Database
```

---

## 2. Technology Stack

| Layer           | Technology                     | Purpose                                         |
|-----------------|--------------------------------|-------------------------------------------------|
| Frontend        | HTML5 + Bootstrap 5 + Jinja2   | UI rendering and templating                     |
| Language        | Python 3.x                     | Backend logic                                   |
| Framework       | Flask 3.0                      | Web framework, routing, request handling        |
| ORM             | Flask-SQLAlchemy 3.x           | Database abstraction and query building         |
| Migrations      | Flask-Migrate (Alembic)        | Database schema version control                 |
| Authentication  | Flask-Login + Werkzeug         | Session management and password hashing         |
| Database        | MySQL                          | Persistent relational data storage              |
| DB Driver       | PyMySQL                        | MySQL connector for Python                      |
| Config          | python-dotenv                  | Environment variable management                 |
| Testing         | Pytest                         | Automated test runner                           |
| Deployment      | Localhost → Render (planned)   | Development and production hosting              |
| Version Control | Git + GitHub                   | Source code management                          |
| IDE             | Visual Studio Code             | Development environment                         |

---

## 3. Folder Structure

The project follows a blueprint-based modular folder structure.

```text
SmartStock/
│
├── app/
│   ├── __init__.py              # Flask app factory
│   ├── extensions.py            # Flask extensions (db, login_manager, migrate)
│   ├── models/
│   │   └── __init__.py          # All SQLAlchemy models
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── auth.py              # Login / Logout
│   │   ├── dashboard.py         # Dashboard statistics
│   │   ├── category.py          # Category CRUD
│   │   ├── product.py           # Product management
│   │   ├── inventory.py         # Stock adjustments and history
│   │   ├── billing.py           # POS and checkout API
│   │   ├── sales.py             # Sales history and invoices
│   │   └── customer.py          # Customer management
│   ├── services/                # Business logic layer (planned)
│   │   └── __init__.py
│   ├── templates/               # Jinja2 HTML templates
│   │   ├── base.html            # Base layout with navbar
│   │   ├── auth/
│   │   ├── dashboard/
│   │   ├── category/
│   │   ├── product/
│   │   ├── inventory/
│   │   ├── billing/
│   │   ├── sales/
│   │   └── customer/
│   ├── static/
│   │   ├── css/                 # Custom CSS
│   │   ├── js/                  # Custom JavaScript
│   │   └── images/              # Static images and logos
│   └── utils/                   # Helper functions, decorators
│       └── __init__.py
│
├── tests/                       # Pytest test cases
├── migrations/                  # Alembic migration files
├── config.py                    # Flask configuration class
├── run.py                       # Application entry point
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables (not committed)
├── .gitignore                   # Git ignore rules
├── PRD.md                       # Product Requirements Document
├── ARCHITECTURE.md              # This file
├── DESIGN.md                    # Design system and UI guidelines
├── RULES.md                     # Development rules and coding standards
├── TASKS.md                     # Project task list and status
├── MEMORY.md                    # Project memory and progress tracker
└── README.md                    # Project overview and setup guide
```

---

## 4. Database Schema

### Tables and Relationships

```
users ──────────────────────────────────────────────────────┐
  │                                                          │
  ├── sales (user_id FK)                                     │
  └── inventory_transactions (user_id FK)                    │
                                                             │
categories                                                   │
  └── products (category_id FK)                             │
          │                                                  │
          ├── sale_items (product_id FK)                     │
          └── inventory_transactions (product_id FK)         │
                                                             │
customers                                                    │
  └── sales (customer_id FK, nullable)                       │
          └── sale_items (sale_id FK) ───────────────────────┘

shop_settings (single configuration row)
```

### Field Types for Financial Data
All price, tax, discount, and total fields use `DECIMAL(10, 2)` — never FLOAT — to ensure exact arithmetic for billing calculations.

---

## 5. Key Design Decisions

### Blueprint-Based Architecture
Each module (auth, product, billing, etc.) is registered as an independent Flask Blueprint. This keeps routes, templates, and logic separated and scalable.

### Application Factory Pattern
The Flask app is created inside a `create_app()` factory in `app/__init__.py`. Extensions are initialized in `app/extensions.py` to prevent circular imports.

### Soft Delete (Deactivation)
Products and categories use an `is_active` boolean flag instead of hard deletion. This preserves the integrity of historical invoices and sale records.

### Inventory Audit Trail
Every stock change (sale, stock-in, manual adjustment) creates an `InventoryTransaction` record. Stock is never silently modified.

### Server-Side Validation
All business rules (stock checks, price validation, duplicate SKU) are enforced at the Flask route level, independent of any frontend validation.

### Role-Based Access Control
Admin-only actions (adding/deactivating products, categories, manual stock adjustments) are guarded with `current_user.role != 'Admin'` checks in every route.
