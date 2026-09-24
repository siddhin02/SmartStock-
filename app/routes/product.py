from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Product, Category
from app.extensions import db
import os

bp = Blueprint('product', __name__, url_prefix='/products')


@bp.route('/')
@login_required
def index():
    products = Product.query.order_by(Product.name).all()
    return render_template('product/index.html', products=products)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if current_user.role != 'Admin':
        flash('Only administrators can add products.', 'danger')
        return redirect(url_for('product.index'))

    if request.method == 'POST':
        name = request.form.get('name').strip()
        category_id = request.form.get('category_id')
        sku = request.form.get('sku').strip() or None
        barcode = request.form.get('barcode').strip() or None
        purchase_price = request.form.get('purchase_price')
        selling_price = request.form.get('selling_price')
        stock_quantity = request.form.get('stock_quantity')
        min_stock_level = request.form.get('min_stock_level')
        unit = request.form.get('unit')
        
        if sku and Product.query.filter_by(sku=sku).first():
            flash('A product with this SKU already exists.', 'warning')
            return redirect(url_for('product.add'))
            
        if barcode and Product.query.filter_by(barcode=barcode).first():
            flash('A product with this Barcode already exists.', 'warning')
            return redirect(url_for('product.add'))
            
        new_product = Product(
            name=name,
            category_id=category_id,
            sku=sku,
            barcode=barcode,
            purchase_price=purchase_price,
            selling_price=selling_price,
            stock_quantity=stock_quantity,
            min_stock_level=min_stock_level,
            unit=unit
        )
        db.session.add(new_product)
        db.session.flush() # Flush to get the new_product.id before commit
        
        # BUSINESS RULE: Stock changes should be traceable
        if int(stock_quantity) > 0:
            from app.models import InventoryTransaction
            txn = InventoryTransaction(
                product_id=new_product.id,
                user_id=current_user.id,
                transaction_type='Stock-in',
                quantity_changed=int(stock_quantity),
                reference_id='Initial Stock Creation'
            )
            db.session.add(txn)
            
        db.session.commit()
        flash(f'Product "{name}" added successfully!', 'success')
        return redirect(url_for('product.index'))
        
    categories = Category.query.filter_by(is_active=True).order_by(Category.name).all()
    return render_template('product/add.html', categories=categories)













