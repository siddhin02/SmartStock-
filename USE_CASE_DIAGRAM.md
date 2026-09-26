# SmartStock - Use Case Diagram

```mermaid
flowchart LR
    Guest([Guest])
    Staff([Staff])
    Admin([Admin])

    Guest --> Register[Register]
    Guest --> Login[Login]

    Staff --> Login
    Admin --> Login

    Staff --> Dashboard[View Dashboard]
    Admin --> Dashboard

    Staff --> ProductList[View Products]
    Admin --> ProductList
    Admin --> AddProduct[Add Products]

    Staff --> Billing[Use Billing POS]
    Admin --> Billing

    Staff --> Customers[Manage Customers]
    Admin --> Customers

    Staff --> SalesHistory[View Sales History]
    Admin --> SalesHistory

    Staff --> Reports[View Reports]
    Admin --> Reports

    Admin --> Categories[Manage Categories]
    Admin --> Inventory[Adjust Inventory]
    Admin --> UserManagement[Manage Users]
    Admin --> CreateStaff[Create Staff Users]
    Admin --> ToggleStaff[Activate / Deactivate Staff]

    Staff --> Logout[Logout]
    Admin --> Logout