# SmartStock - Entity Relationship Diagram

```mermaid
erDiagram
    USER ||--o{ SALE : creates
    USER ||--o{ INVENTORY_TRANSACTION : records
    CUSTOMER ||--o{ SALE : has
    SALE ||--|{ SALE_ITEM : contains
    PRODUCT ||--o{ SALE_ITEM : references
    CATEGORY ||--o{ PRODUCT : contains
    PRODUCT ||--o{ INVENTORY_TRANSACTION : tracks

    USER {
        int id PK
        string username UK
        string password_hash
        string role
        boolean is_active
        datetime created_at
    }

    CATEGORY {
        int id PK
        string name UK
        boolean is_active
    }

    PRODUCT {
        int id PK
        int category_id FK
        string name
        string sku UK
        string barcode UK
        decimal purchase_price
        decimal selling_price
        int stock_quantity
        int min_stock_level
        string unit
        decimal tax_percentage
        boolean is_active
        datetime created_at
        datetime updated_at
    }

    CUSTOMER {
        int id PK
        string name
        string mobile UK
        string email
        text address
    }

    SALE {
        int id PK
        string invoice_number UK
        int user_id FK
        int customer_id FK
        decimal subtotal
        decimal total_tax
        decimal total_discount
        decimal grand_total
        string payment_method
        string status
        datetime created_at
    }

    SALE_ITEM {
        int id PK
        int sale_id FK
        int product_id FK
        int quantity
        decimal unit_price
        decimal tax_amount
        decimal line_total
    }

    INVENTORY_TRANSACTION {
        int id PK
        int product_id FK
        int user_id FK
        string transaction_type
        int quantity_changed
        string reference_id
        datetime created_at
    }

    SHOP_SETTINGS {
        int id PK
        string shop_name
        string owner_name
        text address
        string phone
        string email
        string gstin
        string currency
        string invoice_prefix
    }