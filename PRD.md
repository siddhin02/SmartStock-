# Product Requirements Document (PRD)

## SmartStock – Inventory & Billing Software for Local Shop

**Version:** 1.0
**Date:** September 2026
**Author:** SmartStock Development Team
**Status:** In Development
**Target Launch:** MVP (v1.0)

---

## 1. Product Overview

SmartStock is a web-based inventory management and billing application designed for small and local shop owners. It replaces manual notebooks and spreadsheets with a fast, secure, and organized digital system.

---

## 2. Problem Statement

Many small shop owners manage product stock, sales, and billing information manually using notebooks or basic spreadsheets. This causes:

- Calculation mistakes in bills
- Difficulty tracking available stock
- Missing sales records
- Inability to understand daily or monthly business performance
- No audit trail for stock movements

---

## 3. Goals

- Help shop owners manage products digitally
- Maintain accurate stock information
- Generate customer bills quickly
- Automatically update inventory after sales
- Maintain a complete sales history
- Monitor low-stock and out-of-stock products
- Provide daily, weekly, and monthly business reports
- Reduce manual work and make everyday shop management faster and more organized

---

## 4. Target Users

### Primary User – Shop Owner / Administrator
Complete access to:
- Dashboard, Products, Categories, Inventory
- Billing, Sales Records, Customers
- Reports, User Management, Settings

### Secondary User – Cashier / Staff
Limited access to:
- Product search
- Billing (Point of Sale)
- Customer details
- Sales transactions

Administrative functions (deleting products, sensitive reports, user management) are restricted for Staff.

---

## 5. Core Features (MVP)

### 5.1 Authentication
- Admin and Staff login
- Secure logout
- Password hashing (Werkzeug)
- Session management (Flask-Login)
- Role-based access control (Admin / Staff)
- Invalid login validation

### 5.2 Dashboard
- Total products count
- Total available stock
- Low-stock and out-of-stock alerts
- Today's sales total
- Today's number of bills
- Monthly sales total
- Recent transactions list

### 5.3 Category Management
- Add, view, deactivate/activate categories
- Examples: Groceries, Beverages, Snacks, Personal Care, Household Items, Stationery

### 5.4 Product Management
- Add, view, edit, deactivate products
- Fields: Name, Category, SKU, Barcode, Purchase Price, Selling Price, Stock Quantity, Min Stock Level, Unit, Tax %, Status
- Duplicate SKU/Barcode validation

### 5.5 Inventory Management
- Current stock tracking
- Stock-in, Stock-out, Adjustment transactions
- Low-stock and out-of-stock warnings
- Full inventory transaction history (audit trail)

### 5.6 Customer Management
- Add, search, view customers
- Customer purchase history
- Walk-in billing support (no customer required)

### 5.7 Billing / Point of Sale (POS)
- Fast product search (name, SKU, barcode)
- Add to cart, update quantity, remove items
- Automatic subtotal and grand total calculation
- Payment method selection (Cash, UPI, Card)
- Unique invoice number generation
- Automatic stock deduction on checkout
- Inventory transaction logged per sale

### 5.8 Sales Management
- Complete sales history
- Filter by invoice number, payment method, date range
- View individual invoice details
- Printable invoice (print-friendly CSS)

### 5.9 Reports
- Daily, weekly, monthly sales reports
- Low-stock report
- Inventory movement report

### 5.10 Shop Settings
- Shop name, owner name, address, phone, email, GSTIN
- Currency (default: ₹ INR)
- Invoice prefix

---

## 6. Business Rules

1. Product stock must not go negative accidentally.
2. Completing a sale must deduct inventory and log an InventoryTransaction.
3. Invoice numbers must be unique.
4. SKU/Barcode values must be unique when provided.
5. Prices and quantities cannot be negative.
6. Billing totals must be calculated accurately using Decimal arithmetic.
7. Unauthorized users must not access admin functionality.
8. Passwords must be hashed (never stored as plain text).
9. Critical database operations must use transactions to ensure data consistency.
10. Historical invoice data must remain correct even if a product is later renamed or deleted.
11. Deleting/deactivating a product must not corrupt old invoice records.
12. Server-side validation is mandatory regardless of frontend validation.

---

## 7. Future Enhancements (Post-MVP)

- PDF invoice download
- Barcode scanner integration
- WhatsApp invoice sharing
- Supplier and purchase order management
- Expense tracking and profit/loss dashboard
- Multiple shop/branch support
- Advanced analytics
- Cloud backup and automated low-stock alerts
- GST filing reports
- Offline-capable mobile POS
