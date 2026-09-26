# SmartStock

## Inventory & Billing Software for Local Shop

**Final Project Report**

**Version:** 1.0
**Date:** September 2026
**Project:** SmartStock
**Application Type:** Web-based Inventory Management and Billing System

---

## 1. Abstract

SmartStock is a web-based inventory management and billing application designed for small and local shop owners.

The system replaces manual notebooks and basic spreadsheets with a centralized digital system for managing products, categories, inventory, customers, billing, sales history, reports, and users.

The application is developed using Python Flask, MySQL, SQLAlchemy, Flask-Login, Bootstrap 5, Jinja2, and Pytest. It provides role-based access for Admin and Staff users, automatic inventory deduction after sales, inventory transaction tracking, sales reporting, customer management, and administrative user management.

The system follows a server-rendered MVC-style architecture using Flask Blueprints and SQLAlchemy. Production deployment is configured using Render for application hosting and Aiven MySQL for the database.

---

## 2. Introduction

Small shops often manage inventory, billing, and sales information manually. This approach can make it difficult to maintain accurate stock levels, preserve sales records, and understand business performance.

SmartStock was developed to provide a structured digital solution for these operational requirements.

The application combines inventory management and Point of Sale billing in a single web-based system. It also provides reporting and customer management features while restricting administrative operations through role-based access control.

---

## 3. Problem Statement

The project addresses common problems faced by small shop owners when using notebooks or basic spreadsheets:

* Calculation mistakes in bills
* Difficulty tracking available stock
* Missing sales records
* Difficulty understanding daily or monthly business performance
* Lack of an audit trail for stock movements
* Manual and repetitive shop management activities

SmartStock addresses these problems by maintaining centralized digital records and automating important inventory and billing operations.

---

## 4. Project Objectives

The main objectives of SmartStock are:

1. Digitally manage shop products and inventory.
2. Maintain accurate stock information.
3. Generate customer bills efficiently.
4. Automatically update inventory after completed sales.
5. Maintain complete sales history.
6. Monitor low-stock and out-of-stock products.
7. Provide business reports.
8. Reduce manual work in everyday shop management.
9. Provide role-based access for Admin and Staff users.
10. Maintain an inventory audit trail for stock movements.

---

## 5. Target Users

### 5.1 Admin

The Admin has complete access to the application's administrative and operational functions, including:

* Dashboard
* Categories
* Products
* Inventory
* Billing POS
* Customers
* Sales History
* Reports
* User Management
* Staff user creation
* Staff activation and deactivation

### 5.2 Staff

Staff users are intended for day-to-day operational activities such as:

* Product search
* Billing and sales transactions
* Customer operations
* Sales history
* Reports

Administrative functions such as User Management are restricted to Admin users.

---

## 6. Functional Features

### 6.1 Authentication

SmartStock provides:

* User login
* User registration
* Secure logout
* Password hashing using Werkzeug
* Session management using Flask-Login
* Admin and Staff roles
* Inactive-account protection
* Invalid login validation

New registrations are created as Staff accounts.

### 6.2 Dashboard

The Dashboard provides an overview of inventory and sales information, including:

* Active products
* Units in stock
* Low-stock products
* Out-of-stock products
* Sales statistics
* Sales-related visual information

### 6.3 Category Management

The category module allows authorized users to:

* View categories
* Add categories
* Activate categories
* Deactivate categories

### 6.4 Product Management

The product module provides product catalogue management.

Product information includes:

* Product name
* Category
* SKU
* Barcode
* Purchase price
* Selling price
* Stock quantity
* Minimum stock level
* Unit
* Tax percentage
* Active status

The system validates duplicate SKU and barcode values.

### 6.5 Inventory Management

The inventory module provides:

* Current stock tracking
* Stock adjustments
* Stock movement history
* Inventory transaction records
* Low-stock monitoring

Inventory transactions record stock movements such as:

* Stock-in
* Stock-out
* Adjustment
* Sale

### 6.6 Customer Management

Customer management includes:

* Adding customers
* S
