# Development Rules

## SmartStock – Project Guidelines for AI & Human Collaboration

This document defines the development rules, coding standards, and best practices for building SmartStock. These rules ensure consistency, maintainability, security, and high-quality code.

Both AI assistants and human contributors must follow these guidelines.

---

## 1. GENERAL PRINCIPLES

- Follow the project documentation (PRD.md, ARCHITECTURE.md, DESIGN.md) before making changes.
- Keep the code clean, readable, and well-structured.
- Prioritize simplicity and maintainability over cleverness.
- Do not duplicate logic. Reuse existing models, utilities, or services.
- Make small, focused changes instead of large risky edits.
- Do not modify unrelated files.
- Write self-explanatory code with meaningful variable and function names.

---

## 2. INSPECT BEFORE CHANGING (Rule A)

Before modifying anything:
1. Identify the relevant files.
2. Inspect their current contents.
3. Understand dependencies.
4. Identify what could break.
5. Only then propose or make the change.

**Never rewrite an entire module because one small part needs fixing.**

---

## 3. PRESERVE EXISTING FUNCTIONALITY (Rule B)

If backend and frontend are already connected, DO NOT change:
- Flask route URLs
- HTTP methods (GET/POST)
- API response field names
- Database column names
- Model relationships
- Template variable names that work

If a change is necessary, document:
> **WHY → WHAT WILL CHANGE → WHAT COULD BREAK → HOW WE WILL TEST IT**

---

## 4. ONE STEP AT A TIME (Rule C)

Work cycle:
```
BACKUP → INSPECT → CHANGE → RUN → TEST → VISUAL TEST → PASS
```
Never provide 10 implementation steps at once. Give one step, wait for the result.

---

## 5. TECHNOLOGY & CODING STANDARDS

**Language:** Python 3.x. Use type hints where it aids clarity.

**Framework:** Flask 3.x, App Factory pattern, Blueprints per module.

**Database:** MySQL via SQLAlchemy ORM. Never write raw SQL unless absolutely necessary.

**Financial Values:** Always use `DECIMAL(10, 2)` / Python `Decimal`. Never use float for money.

**Templates:** Jinja2 with Bootstrap 5. Follow the component conventions in DESIGN.md.

**Styling:** Bootstrap 5 utility classes. Avoid inline `style=""` unless strictly needed.

**Validation:** Server-side validation in every route. Frontend validation is a UX aid only.

**Passwords:** Always use `werkzeug.security.generate_password_hash` / `check_password_hash`. Never store plain text.

**Sessions:** Always use `@login_required` decorator on protected routes.

**Role Checks:** Use `current_user.role != 'Admin'` check at the start of admin-only routes.

---

## 6. BUSINESS RULES (Mandatory)

These must be enforced in every relevant route:

| Rule | Where Enforced |
|------|----------------|
| Stock cannot go negative | `billing.py`, `inventory.py` |
| Sale must log InventoryTransaction | `billing.py` |
| Stock adjustment must log InventoryTransaction | `inventory.py` |
| Invoice numbers must be unique | `billing.py` (UUID-based) |
| SKU/Barcode must be unique | `product.py` (query before insert) |
| Prices cannot be negative | HTML `min="0"` + server check |
| Admin-only actions blocked for Staff | Every relevant route |

---

## 7. PROJECT STRUCTURE

- Reusable query logic → `app/services/`
- Template filters and small helpers → `app/utils/`
- Each module has its own Blueprint file in `app/routes/`
- Each module has its own templates folder in `app/templates/<module>/`
- Do not put business logic inside templates.
- Do not put database queries inside templates.

---

## 8. GIT WORKFLOW

Use feature branches:
```
feature/authentication
feature/product-management
feature/inventory
feature/billing
feature/dashboard
feature/reports
fix/billing-calculation
ui/dashboard
```

Before major changes:
```powershell
git status -sb
git branch --show-current
git log --oneline -5
```

Before committing:
```powershell
git diff
```

Commit message format:
```
feat: add inventory adjustment route
fix: prevent negative stock on checkout
ui: improve billing POS layout
chore: update requirements.txt
```

---

## 9. DEBUGGING RULES

When an error occurs:
1. Read the complete traceback.
2. Identify the root cause.
3. Make the smallest possible fix.
4. Run the application again.
5. Test the affected feature.
6. Check for regressions.

Never randomly change multiple files to fix one error.

---

## 10. TERMINAL (Windows + PowerShell)

Always activate the virtual environment first:
```powershell
.\venv\Scripts\Activate.ps1
```

Common commands:
```powershell
flask run                          # Start development server
flask db migrate -m "description"  # Create migration
flask db upgrade                   # Apply migration
pytest tests/                      # Run tests
```
