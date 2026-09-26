# SmartStock User Manual

## 1. Introduction

SmartStock is a web-based inventory management and billing application for small and local shops.

The system provides:

* Inventory and product management
* Point of Sale (POS) billing
* Customer management
* Sales history
* Inventory tracking
* Reports
* Dashboard statistics
* Admin and Staff role-based access

---

## 2. Getting Started

### 2.1 Login

Open the SmartStock application in a web browser.

Enter your:

* Username
* Password

Select **Login**.

If the credentials are correct and the account is active, SmartStock opens the Dashboard.

If an account has been deactivated, login is blocked and the user is instructed to contact the administrator.

### 2.2 Registration

New users can select the registration option and provide:

* Username
* Password
* Confirm password

The username must be unique and the passwords must match.

A newly registered account is created as a **Staff** user and can then be used to log in.

### 2.3 Logout

Select **Logout** from the navigation bar to end the current session and return to the login page.

---

## 3. User Roles

### 3.1 Admin

Administrators can access:

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

Administrators can also add products, manage categories, and adjust inventory.

### 3.2 Staff

Staff users can perform permitted day-to-day operational activities such as:

* Product search
* Billing and sales transactions
* Customer operations
* Sales history
* Reports

Administrative functions such as User Management are restricted to Admin users.

---

## 4. Dashboard

After logging in, the Dashboard provides an overview of the shop's current information.

The dashboard includes inventory statistics such as:

* Active products
* Units in stock
* Low-stock products
* Out-of-stock products

The dashboard also provides sales-related visual information.

Use the navigation bar to move between the different SmartStock modules.

---

## 5. Categories

The Categories section allows authorized users to manage product categories.

### 5.1 View Categories

Open **Categories** from the navigation bar to view the available categories.

### 5.2 Add a Category

Enter the category information and submit the form.

### 5.3 Activate or Deactivate a Category

Authorized users can change a category's active status.

A confirmation message is displayed before changing the category status.

---

## 6. Products

The Products section provides access to the product catalogue.

### 6.1 View Products

Open **Products** to view the available products.

Product information includes details such as:

* Product name
* Category
* SKU
* Barcode
* Purchase price
* Selling price
* Stock quantity
* Minimum stock level
* Unit

### 6.2 Add a Product

Administrators can select the product creation option and enter the required product information.

SmartStock validates duplicate SKU and barcode values.

When a product is created with initial stock, the stock-in movement is recorded in the inventory transaction history.

---

## 7. Inventory

The Inventory section is used to view and adjust stock quantities.

Administrators can perform inventory adjustments for products.

Inventory changes are recorded as inventory transactions so that stock movements can be traced.

Inventory movements can include:

* Stock-in
* Stock-out
* Adjustment
* Sale

---

## 8. Billing POS

Billing POS is used to create sales transactions.

### 8.1 Search for a Product

Use the product search field in the Billing POS.

Products can be searched using:

* Product name
* SKU
* Barcode

Only active products with available stock are returned by the billing search.

### 8.2 Add Products to the Cart

Select a product from the search results and specify the required quantity.

The available stock is used to validate the requested quantity.

### 8.3 Select Payment Method

Select the appropriate payment method before completing the transaction.

### 8.4 Complete Checkout

Submit the checkout when the cart contains the required products.

SmartStock:

1. Validates the products.
2. Validates the quantities.
3. Checks available stock.
4. Calculates the sale subtotal.
5. Generates a unique invoice number.
6. Creates the sale and sale items.
7. Deducts sold quantities from stock.
8. Records the stock movement as a Sale transaction.
9. Saves the transaction.

If there is insufficient stock, the checkout is rejected and the transaction is rolled back.

---

## 9. Customers

The Customers section allows users to maintain customer information.

### 9.1 Add a Customer

Enter:

* Customer name
* Mobile number
* Email
* Address

A mobile number that already belongs to another customer cannot be registered again.

### 9.2 Search Customers

Customers can be searched by:

* Name
* Mobile number

### 9.3 View Customer Details

Open a customer record to view the customer's information and purchase history.

---

## 10. Sales History

The Sales section provides access to previous sales transactions.

Sales can be filtered by:

* Invoice number
* Payment method
* From date
* To date

Select an individual sale to view its details and the products included in that transaction.

---

## 11. Reports

The Reports section provides several reporting views.

### 11.1 Sales Report

The Sales Report can be filtered by date range.

It provides:

* Completed sales
* Total revenue
* Total number of bills
* Payment-method summary

### 11.2 Low Stock Report

The Low Stock Report lists active products whose stock quantity is at or below their configured minimum stock level.

Use this report to identify products that require attention.

### 11.3 Inventory Movement Report

The Inventory Movements report can be filtered by:

* Date range
* Movement type

Available movement types include:

* Stock-in
* Stock-out
* Adjustment
* Sale

### 11.4 Inventory Report

The Inventory Report lists active products and calculates the total inventory value using the product purchase price and current stock quantity.

---

## 12. User Management

User Management is available only to Admin users.

### 12.1 Create a Staff User

Select **User Management** and choose **Add Staff User**.

Enter:

* Username
* Password
* Confirm password

The new account is created with the **Staff** role.

### 12.2 Activate or Deactivate a Staff User

Administrators can change the status of other user accounts.

An inactive user cannot log in.

An administrator cannot change the status of their own account.

---

## 13. Navigation

Authenticated users can access the main SmartStock modules from the navigation bar:

* Dashboard
* Categories
* Billing POS
* Products
* Inventory
* Customers
* Sales
* Reports
* Logout

The **User Management** option is displayed only to Admin users.

---

## 14. Security and Validation

SmartStock includes several validation and security controls:

* Passwords are stored using password hashing.
* Login is required for protected application areas.
* Inactive users cannot log in.
* Admin-only functions are protected by role checks.
* Duplicate usernames are rejected.
* Duplicate product SKUs are rejected.
* Duplicate product barcodes are rejected.
* Duplicate customer mobile numbers are rejected.
* Billing prevents quantities greater than available stock.
* Negative stock is prevented.
* Destructive actions use confirmation dialogs where applicable.

---

## 15. Responsive Interface

SmartStock uses a responsive Bootstrap 5 interface.

The application is designed to remain usable across desktop and mobile screen sizes, including:

* Dashboard cards
* Navigation
* Billing POS
* Product and inventory tables
* Sales history
* Customer pages
* Reports

---

## 16. Troubleshooting

### Cannot log in

Check that:

* The username is correct.
* The password is correct.
* The account is active.

If an account is inactive, contact an administrator.

### Product cannot be added

Check that the SKU and barcode are not already assigned to another product.

### Checkout fails because of stock

Check the product's current available stock and reduce the requested quantity if necessary.

### Staff user cannot access User Management

User Management is restricted to Admin users.

### A customer cannot be added

Check whether the supplied mobile number is already registered to another customer.

---

## 17. Support and Maintenance

For development, configuration, testing, and deployment information, refer to the project documentation:

* `README.md`
* `PRD.md`
* `ARCHITECTURE.md`
* `DESIGN.md`
* `RULES.md`
* `TASKS.md`
* `MEMORY.md`

The project also contains the ER diagram and Use Case Diagram documentation created for the project documentation phase.

---

## 18. Conclusion

SmartStock provides an integrated workflow for managing products, inventory, customers, billing, sales, users, and reports.

The system separates administrative functions from day-to-day Staff operations while maintaining inventory transaction records and protecting stock quantities during billing.
