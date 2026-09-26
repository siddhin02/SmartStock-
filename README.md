# SmartStock

**Inventory & Billing Software for Local Shop**

A web-based inventory management and billing application built for small and local shop owners using Python Flask, MySQL, and Bootstrap 5.

---

## Tech Stack

| Layer       | Technology |
|-------------|------------|
| Language    | Python 3.x |
| Framework   | Flask 3.0 |
| Database    | MySQL |
| ORM         | Flask-SQLAlchemy |
| Migrations  | Flask-Migrate (Alembic) |
| Auth        | Flask-Login + Werkzeug |
| Frontend    | Bootstrap 5 + Jinja2 |
| Environment | python-dotenv |
| Testing     | Pytest |
| Deployment  | Render + Aiven MySQL |

---

## Features

- Secure login and logout
- Admin and Staff role-based access control
- User self-registration
- Admin Staff user management
- Password hashing with Werkzeug
- Category management with activate/deactivate support
- Product management with stock tracking
- Duplicate SKU and barcode validation
- Inventory stock-in and stock-out adjustments
- Inventory audit trail for stock movements
- Point of Sale (POS) billing with live product search
- Automatic stock deduction after successful checkout
- Negative stock prevention
- Unique invoice number generation
- Sales history with invoice, payment, and date filters
- Printable invoice view
- Customer management and search
- Customer purchase history
- Dashboard statistics
- Monthly sales chart
- Daily sales report
- Low-stock report
- Inventory movement report
- Responsive Bootstrap 5 interface
- Page titles and meta descriptions
- Confirmation dialogs for destructive actions

---

## User Roles

### Admin

Administrators have complete access to the application, including:

- Dashboard
- Categories
- Products
- Inventory
- Billing POS
- Customers
- Sales History
- Reports
- User Management
- Creating Staff users
- Activating and deactivating Staff users

### Staff

Staff users have access to operational functions such as:

- Product search
- Billing and sales transactions
- Other permitted day-to-day inventory operations

Administrative functions such as User Management are restricted to Admin users.

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/siddhin02/SmartStock-.git
cd SmartStock
```

### 2. Create and activate virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```


### 3. Install dependencies

```powershell
pip install -r requirements.txt


```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://username:password@localhost/smartstock

Do not commit the `.env` file to Git.


```

### 5. Create the MySQL database

Create a MySQL database named `smartstock`:

```sql
CREATE DATABASE smartstock;

```

### 6. Run database migrations

```powershell
flask db upgrade

```

### 7. Create the initial Admin user

Run the following command and change the username/password as needed:

```powershell
python -c "from run import app; from app.models import User; from app.extensions import db; ctx=app.app_context(); ctx.push(); admin=User(username='admin', role='Admin'); admin.set_password('change-this-password'); db.session.add(admin); db.session.commit(); print('Admin user created.')"
```

### 8. Run the application

```powershell
python run.py
```
---
## Testing

Run the full test suite with:

``powershell
python -m pytest -q
``

The test suite covers authentication, product management, billing calculations, stock deduction, role-based access, and negative stock prevention.

---

## Production Deployment

SmartStock is configured for production deployment using:

- Render for application hosting
- Gunicorn as the production WSGI server
- Aiven MySQL for the production database


Production startup command:

```text
gunicorn run:app
```

Production deployment should use the configured environment variables and must not expose database credentials or secret keys in source control.



---

## Project Documentation

| File | Description |
|------|-------------|
| `PRD.md` | Product Requirements Document |
| `ARCHITECTURE.md` | System Architecture and Technology Details |
| `DESIGN.md` | Design System and UI Guidelines |
| `RULES.md` | Development Rules and Standards |
| `TASKS.md` | Project Task Breakdown and Status |
| `MEMORY.md` | Project Progress and Context |


---

## Project Structure

```text
SmartStock/
+-- app/
|   +-- __init__.py
|   +-- extensions.py
|   +-- models/
|   |   +-- __init__.py
|   +-- routes/
|   |   +-- auth.py
|   |   +-- dashboard.py
|   |   +-- category.py
|   |   +-- product.py
|   |   +-- inventory.py
|   |   +-- billing.py
|   |   +-- sales.py
|   |   +-- customer.py
|   |   +-- reports.py
|   |   +-- user.py
|   +-- templates/
|   +-- static/
+-- migrations/
+-- tests/
+-- config.py
+-- run.py
+-- requirements.txt
+-- README.md
+-- .env
```
## License

Student Project - For Educational Use
