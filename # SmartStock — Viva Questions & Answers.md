# SmartStock — Viva Questions & Answers

## 1. What is SmartStock?

**Answer:**
SmartStock is a web-based inventory management and billing application designed for small and local shop owners. It manages products, categories, inventory, customers, billing, sales history, reports, and user access.

---

## 2. What problem does SmartStock solve?

**Answer:**
It replaces manual notebooks and basic spreadsheets with a centralized digital system. It helps reduce billing calculation mistakes, improves stock tracking, maintains sales records, and provides reports for shop operations.

---

## 3. Who are the target users?

**Answer:**
The main users are Admin and Staff.

* **Admin:** Has administrative and operational access.
* **Staff:** Performs permitted day-to-day operational activities but cannot access Admin-only functions.

---

## 4. Which technologies did you use?

**Answer:**

* Python
* Flask
* Flask-SQLAlchemy
* MySQL
* Flask-Migrate / Alembic
* Flask-Login
* Werkzeug
* Jinja2
* Bootstrap 5
* Pytest
* Gunicorn
* Render
* Aiven MySQL

---

## 5. Why did you use Flask?

**Answer:**
Flask provides a lightweight Python web framework suitable for building a modular web application. SmartStock uses Flask Blueprints and an application factory pattern to organize the application into separate functional modules.

---

## 6. What is the architecture of SmartStock?

**Answer:**

The main architecture is:

```text
Browser
   ↓
Flask Frontend
   ↓
Flask Backend / Blueprints
   ↓
SQLAlchemy ORM
   ↓
MySQL Database
```

The frontend uses Jinja2 and Bootstrap 5.

---

## 7. What is a Flask Blueprint?

**Answer:**
A Blueprint is a way of organizing Flask routes into separate modules. SmartStock uses separate route modules for authentication, dashboard, products, categories, inventory, billing, customers, sales, reports, and user management.

---

## 8. What is the application factory pattern?

**Answer:**
The application factory creates and configures the Flask application through a function. It helps keep application initialization modular and makes the project easier to maintain and test.

---

## 9. Which database does SmartStock use?

**Answer:**
SmartStock uses MySQL as its relational database. SQLAlchemy is used as the ORM layer for database operations.

---

## 10. What are the main database entities?

**Answer:**

The main entities are:

* User
* Category
* Product
* Customer
* Sale
* SaleItem
* InventoryTransaction
* ShopSettings

---

## 11. What is the purpose of SaleItem?

**Answer:**
SaleItem stores the individual products included in a sale. It connects a Sale with a Product and stores information such as quantity, unit price, tax amount, and line total.

---

## 12. Why is InventoryTransaction used?

**Answer:**
InventoryTransaction provides an audit trail of stock movements. It records information such as the product, user, transaction type, quantity changed, reference, and creation time.

---

## 13. How does billing work?

**Answer:**

The billing process is:

1. Search for a product.
2. Add the product to the cart.
3. Set the required quantity.
4. Select a payment method.
5. Validate the products and quantities.
6. Check available stock.
7. Generate a unique invoice number.
8. Create the sale and sale items.
9. Deduct the stock.
10. Record the inventory transaction.
11. Commit the transaction.

---

## 14. How does SmartStock prevent negative stock?

**Answer:**
Before completing checkout, the system checks whether the requested quantity is greater than the available stock. If there is insufficient stock, the checkout is rejected and the database transaction is rolled back.

---

## 15. What happens if checkout fails?

**Answer:**
The database transaction is rolled back so that partial changes are not retained.

---

## 16. How is inventory updated after a sale?

**Answer:**
After a valid checkout, the sold quantity is deducted from the product's stock quantity and an InventoryTransaction record is created with the sale reference.

---

## 17. How are invoice numbers generated?

**Answer:**
The billing system generates a unique invoice number using the configured invoice format and current date information.

---

## 18. What payment methods are supported?

**Answer:**
The billing system supports:

* Cash
* UPI
* Card

---

## 19. How is authentication implemented?

**Answer:**
Flask-Login is used for authentication and session management. Passwords are stored using secure Werkzeug password hashing.

---

## 20. How does role-based access control work?

**Answer:**
The application checks the authenticated user's role before allowing access to Admin-only functions.

Admin-only functions include:

* Adding products
* Category management
* Inventory adjustment
* User Management
* Creating Staff users
* Activating or deactivating Staff users

---

## 21. Can a Staff user create another user?

**Answer:**
No. User creation is restricted to Admin users.

---

## 22. Can an Admin deactivate their own account?

**Answer:**
No. The implementation prevents an Admin from changing the status of their own account.

---

## 23. What happens when an inactive user tries to log in?

**Answer:**
The login is rejected and the user is informed that the account is inactive and that they should contact the administrator.

---

## 24. How does user registration work?

**Answer:**
A user provides a username, password, and password confirmation. The system validates the information, checks for duplicate usernames, hashes the password, and creates the new account as an active Staff user.

---

## 25. How are duplicate products prevented?

**Answer:**
SKU and barcode fields are unique, and the application validates duplicate values before creating product records.

---

## 26. How are customers managed?

**Answer:**
Users can add and search customers, view customer details, and view their sales history. Customer mobile numbers are validated to prevent duplicate customer records.

---

## 27. What reports are available?

**Answer:**

SmartStock provides:

* Sales Report
* Low Stock Report
* Inventory Movement Report
* Inventory Report

The Sales Report supports date-range filtering and payment-method summaries.

---

## 28. What is the purpose of the Dashboard?

**Answer:**
The Dashboard gives a quick overview of important inventory and sales information, including active products, stock levels, low-stock products, out-of-stock products, and sales information.

---

## 29. How did you test the project?

**Answer:**
Pytest was used for automated testing. Tests cover authentication, product management, billing calculations, stock deduction, role-based access, and negative stock prevention.

The latest full regression result was:

```text
31 passed, 80 warnings
```

There were no test failures.

---

## 30. What were the warnings in the test results?

**Answer:**
The warnings were existing SQLAlchemy deprecation warnings. They did not cause test failures.

---

## 31. How is the application deployed?

**Answer:**
The application is configured for production using Render and Gunicorn, with Aiven MySQL used for the production database.

The WSGI target is:

```text
gunicorn run:app
```

---

## 32. How are sensitive configuration values handled?

**Answer:**
Sensitive values such as the secret key and database connection information are provided through environment variables and are not stored in source control.

---

## 33. What is the purpose of Flask-Migrate?

**Answer:**
Flask-Migrate uses Alembic to manage database schema migrations. It allows database structure changes to be tracked and applied in a controlled manner.

---

## 34. Why use SQLAlchemy?

**Answer:**
SQLAlchemy provides an ORM layer that allows the application to work with database entities using Python models while maintaining relationships between the database tables.

---

## 35. How is the application responsive?

**Answer:**
Bootstrap 5 responsive components are used throughout the interface. Dashboard cards, navigation, billing layouts, and tables were tested on smaller screen sizes.

---

## 36. What are the main limitations of the current project?

**Answer:**
The PRD identifies several future enhancements that are not currently implemented, including:

* PDF invoice download
* Barcode scanner integration
* WhatsApp invoice sharing
* Supplier and purchase-order management
* Expense and profit/loss features
* Multiple branches
* Advanced analytics
* Cloud backup and alerts
* GST reports
* Offline mobile POS

---

## 37. What was the most important business rule implemented?

**Answer:**
One important rule is that a sale must not result in negative stock. The system validates available stock before checkout and updates inventory only when the transaction succeeds.

---

## 38. What happens to historical sales if a product is deactivated?

**Answer:**
Products use an active/inactive status rather than requiring deletion for normal deactivation. This allows historical transaction records to remain associated with their existing product and sale data.

---

## 39. What is the purpose of soft deletion or deactivation?

**Answer:**
Deactivation allows a product or category to stop being used operationally without removing the record and potentially affecting historical information.

---

## 40. What did you learn from this project?

**Answer:**
The project provided practical experience with Flask application architecture, database design, authentication, role-based access control, inventory management, billing workflows, database migrations, automated testing, responsive UI design, and production deployment.

---

# Quick Viva Revision

## Remember These 10 Points

1. **Project:** SmartStock — Inventory & Billing Software.
2. **Backend:** Python + Flask.
3. **Database:** MySQL.
4. **ORM:** SQLAlchemy.
5. **Authentication:** Flask-Login + Werkzeug password hashing.
6. **Frontend:** Jinja2 + Bootstrap 5.
7. **Testing:** Pytest.
8. **Deployment:** Render + Gunicorn + Aiven MySQL.
9. **Important rule:** Prevent negative stock.
10. **Latest tests:** 31 passed.

---

# One-Minute Project Introduction

> SmartStock is a web-based inventory management and billing system designed for small and local shops. It replaces manual notebooks and basic spreadsheets with a centralized application for managing products, categories, inventory, customers, billing, sales history, reports, and users. The application is developed using Python Flask, MySQL, SQLAlchemy, Flask-Login, Jinja2, Bootstrap 5, and Pytest. It provides Admin and Staff roles with role-based access control. One of its important business rules is preventing negative stock during billing while automatically recording inventory movements. The project has been tested using automated Pytest cases and is configured for production deployment using Render and Aiven MySQL.
