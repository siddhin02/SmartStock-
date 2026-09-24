# SmartStock

**Inventory & Billing Software for Local Shop**

A web-based inventory management and billing application built for small and local shop owners using Python Flask, MySQL, and Bootstrap 5.

---

## Tech Stack

| Layer          | Technology              |
|----------------|-------------------------|
| Language       | Python 3.x              |
| Framework      | Flask 3.0               |
| Database       | MySQL                   |
| ORM            | Flask-SQLAlchemy         |
| Migrations     | Flask-Migrate (Alembic)  |
| Auth           | Flask-Login + Werkzeug  |
| Frontend       | Bootstrap 5 + Jinja2    |
| Environment    | python-dotenv           |
| Testing        | Pytest                  |

---

## Features

- ✅ Secure login and logout (Admin / Staff roles)
- ✅ Category management
- ✅ Product management with stock tracking
- ✅ Inventory audit trail (every stock movement logged)
- ✅ Point of Sale (POS) billing with live product search
- ✅ Automatic stock deduction on checkout
- ✅ Unique invoice number generation
- ✅ Sales history with search and date filters
- ✅ Printable invoice view
- ✅ Customer management with purchase history
- 🔄 Dashboard statistics (in progress)
- ⏳ Reports module (planned)

---

## Setup & Installation

### 1. Clone the repository
```bash
git clone <your-repo-url>
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
Create a `.env` file in the root folder:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/smartstock
```

### 5. Create MySQL database
```sql
CREATE DATABASE smartstock;
```

### 6. Run database migrations
```powershell
flask db upgrade
```

### 7. Create the default admin user
```powershell
python -c "
from run import app
from app.models import User
from app.extensions import db
ctx = app.app_context(); ctx.push()
admin = User(username='admin', role='Admin')
admin.set_password('admin123')
db.session.add(admin); db.session.commit()
print('Admin user created.')
"
```

### 8. Run the application
```powershell
flask run
```
Open: `http://127.0.0.1:5000`

**Default login:** `admin` / `admin123`

---

## Project Documentation

| File | Description |
|------|-------------|
| [PRD.md](PRD.md) | Product Requirements Document |
| [ARCHITECTURE.md](ARCHITECTURE.md) | System Architecture & Tech Stack |
| [DESIGN.md](DESIGN.md) | Design System & UI Guidelines |
| [RULES.md](RULES.md) | Development Rules & Standards |
| [TASKS.md](TASKS.md) | Task Breakdown & Status |
| [MEMORY.md](MEMORY.md) | Project Progress & Context |

---

## Project Structure

```text
SmartStock/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models/__init__.py
│   ├── routes/
│   │   ├── auth.py
│   │   ├── dashboard.py
│   │   ├── category.py
│   │   ├── product.py
│   │   ├── inventory.py
│   │   ├── billing.py
│   │   ├── sales.py
│   │   └── customer.py
│   ├── templates/
│   └── static/
├── migrations/
├── config.py
├── run.py
├── requirements.txt
└── .env
```

---

## License

Student Project – For Educational Use
