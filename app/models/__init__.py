from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='Staff', nullable=False) # 'Admin' or 'Staff'
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sales = db.relationship('Sale', backref='cashier', lazy='dynamic')
    inventory_transactions = db.relationship('InventoryTransaction', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    products = db.relationship('Product', backref='category', lazy='dynamic')

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    name = db.Column(db.String(150), nullable=False)
    sku = db.Column(db.String(64), unique=True, index=True)
    barcode = db.Column(db.String(128), unique=True, index=True)
    purchase_price = db.Column(db.Numeric(10, 2), nullable=False)
    selling_price = db.Column(db.Numeric(10, 2), nullable=False)
    stock_quantity = db.Column(db.Integer, default=0, nullable=False)
    min_stock_level = db.Column(db.Integer, default=5)
    unit = db.Column(db.String(20), default='pcs')
    tax_percentage = db.Column(db.Numeric(5, 2), default=0.00)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    sale_items = db.relationship('SaleItem', backref='product', lazy='dynamic')
    inventory_transactions = db.relationship('InventoryTransaction', backref='product', lazy='dynamic')

class Customer(db.Model):
    __tablename__ = 'customers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    mobile = db.Column(db.String(20), unique=True, index=True)
    email = db.Column(db.String(120))
    address = db.Column(db.Text)

    sales = db.relationship('Sale', backref='customer', lazy='dynamic')

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(64), unique=True, index=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)
    total_tax = db.Column(db.Numeric(10, 2), default=0.00)
    total_discount = db.Column(db.Numeric(10, 2), default=0.00)
    grand_total = db.Column(db.Numeric(10, 2), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), default='Completed')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship('SaleItem', backref='sale', lazy='dynamic', cascade='all, delete-orphan')

class SaleItem(db.Model):
    __tablename__ = 'sale_items'
    id = db.Column(db.Integer, primary_key=True)
    sale_id = db.Column(db.Integer, db.ForeignKey('sales.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)
    tax_amount = db.Column(db.Numeric(10, 2), default=0.00)
    line_total = db.Column(db.Numeric(10, 2), nullable=False)

class InventoryTransaction(db.Model):
    __tablename__ = 'inventory_transactions'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)
    quantity_changed = db.Column(db.Integer, nullable=False)
    reference_id = db.Column(db.String(64))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ShopSettings(db.Model):
    __tablename__ = 'shop_settings'
    id = db.Column(db.Integer, primary_key=True)
    shop_name = db.Column(db.String(150), default='SmartStock POS')
    owner_name = db.Column(db.String(150))
    address = db.Column(db.Text)
    phone = db.Column(db.String(20))
    email = db.Column(db.String(120))
    gstin = db.Column(db.String(50))
    currency = db.Column(db.String(10), default='INR')
    invoice_prefix = db.Column(db.String(10), default='INV-')


