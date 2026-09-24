# Project Memory

## SmartStock – Context, Progress & Important Notes

This document tracks the current state of the project, important context, decisions, and continuity information across development sessions.

---

## LAST UPDATED
September 21, 2026

## CURRENT PHASE
Phase 7 – Dashboard & Reports

## OVERALL PROGRESS
~49%

## PROJECT STATUS
In Active Development — MVP v1.0

---

## CURRENT STATUS

- ✅ Project structure fully scaffolded
- ✅ MySQL database connected and all 8 tables migrated
- ✅ Authentication complete (Login, Logout, Flask-Login sessions, password hashing)
- ✅ Role-based access control working (Admin vs Staff)
- ✅ Category management complete (Add, View, Activate/Deactivate)
- ✅ Product management complete (Add, View, Soft-delete, Stock badges)
- ✅ Inventory management complete (Stock-in, Stock-out, Adjustment, Full audit history)
- ✅ Billing/POS complete (Live product search, Cart, Checkout API, Invoice generation, Stock deduction)
- ✅ Sales history complete (List, Filters, Invoice detail, Print invoice)
- ✅ Customer management complete (Add, List, Search, Purchase history)
- ✅ Dashboard statistics — real DB aggregation queries implemented and verified in browser
- ⏳ Reports module — not yet started

---

## COMPLETED TASKS

| Phase | Task | Completed |
|-------|------|-----------|
| 1 | Planning & documentation | Sep 19, 2026 |
| 2 | Project scaffolding, venv, dependencies | Sep 19, 2026 |
| 2 | MySQL connection and all model migrations | Sep 19, 2026 |
| 3 | Login, Logout, Flask-Login, password hashing | Sep 19, 2026 |
| 3 | Bootstrap 5 base template + navbar | Sep 20, 2026 |
| 4 | Category CRUD | Sep 20, 2026 |
| 4 | Product management + inventory transaction on creation | Sep 20, 2026 |
| 4 | Stock adjustment with full audit trail | Sep 20, 2026 |
| 5 | POS Billing — search API, cart, checkout, stock deduction | Sep 20, 2026 |
| 6 | Sales history with filters | Sep 21, 2026 |
| 6 | Printable invoice detail view | Sep 21, 2026 |
| 6 | Customer management + purchase history | Sep 21, 2026 |

---

## IN PROGRESS

| Task | Started | Expected |
|------|---------|----------|
| Dashboard real statistics (Phase 7) | Sep 21, 2026 | Next session |
| Reports module (Phase 7) | Not started | Next session |

---

## IMPORTANT CONTEXT

- SmartStock is a Python/Flask/MySQL/Bootstrap 5 web application.
- The app uses an Application Factory pattern with Flask Blueprints per module.
- Financial values use `DECIMAL(10,2)` — never float.
- Every stock change creates an `InventoryTransaction` record (audit trail).
- Products/Categories use `is_active` soft-delete to preserve historical invoice integrity.
- The default Admin credentials are: **username:** `admin` | **password:** `admin123`
- The `.env` file holds the database URL and secret key (not committed to Git).

---

## KNOWN ISSUES / TO-DO

- Dashboard real aggregation queries implemented and verified.
- Reports module is not yet built.
- Product edit route not yet implemented (only add and view currently).
- No product delete/deactivate from the product list UI (only soft-delete flag exists in DB).
- Billing POS: Customer selection not yet wired to the checkout (walk-in only currently).
- No pagination on large tables (Sales, Products) yet.

---

## DECISIONS & NOTES

- **App Router:** Flask Blueprint pattern selected for clean separation of modules.
- **No frontend framework:** Bootstrap 5 + vanilla JS keeps the project simple and appropriate for a student project.
- **JS in templates:** POS billing uses inline `<script>` with fetch API for the interactive cart. This is acceptable for the scale of this project.
- **Migrations:** Flask-Migrate (Alembic) manages all DB schema changes. Never alter tables directly in MySQL Workbench.
- **UUID invoice numbers:** Format `INV-YYYYMMDD-XXXXXX` ensures uniqueness without a database sequence.

---

## ENVIRONMENT SETUP (Quick Reference)

```powershell
# Navigate to project
cd C:\Users\narva\OneDrive\Desktop\SmartStock

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Run the application
flask run

# Run after model changes
flask db migrate -m "description"
flask db upgrade
```

**Database:** `smartstock` on `localhost`
**MySQL User:** `root`
**App URL:** `http://127.0.0.1:5000`

---

## NEXT STEPS

1. Wire up Dashboard with real DB statistics (today's sales, product count, low stock count).
2. Add a Sales Chart using Chart.js on the dashboard.
3. Build the Reports module (daily sales report, low-stock report).
4. Implement product edit and deactivate from the Products list UI.
5. Add product search/filter on the Products page.
6. Wire customer selection in the Billing POS checkout.
7. Write test cases (Phase 8).
8. UI polish pass (Phase 9).
9. Deployment to Render (Phase 10).

---

## CHANGE LOG

| Date | Changes |
|------|---------|
| Sep 19, 2026 | Project initialized. Scaffolding, venv, dependencies, MySQL connected, all 8 tables migrated, Git initialized. |
| Sep 19, 2026 | Authentication complete. Login/Logout/Flask-Login/hashing. Default admin user created. |
| Sep 20, 2026 | Bootstrap 5 integrated. Dashboard placeholder cards. Category management complete. |
| Sep 20, 2026 | Product management complete with inventory transaction logging on creation. |
| Sep 20, 2026 | Inventory management complete (adjust stock, full audit history). |
| Sep 20, 2026 | Billing/POS complete with live search, cart, checkout API, stock deduction, invoice generation. |
| Sep 21, 2026 | Sales history with filters and printable invoice view complete. |
| Sep 21, 2026 | Customer management complete with purchase history. |
| Sep 21, 2026 | Documentation created: PRD.md, ARCHITECTURE.md, DESIGN.md, RULES.md, TASKS.md, MEMORY.md |

