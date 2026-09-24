from flask import Blueprint, render_template, request, jsonify
from flask_login import login_required, current_user
from app.models import Product, Sale, SaleItem, InventoryTransaction
from app.extensions import db
from datetime import datetime
import uuid

bp = Blueprint('billing', __name__, url_prefix='/billing')

@bp.route('/')
@login_required
def index():
    return render_template('billing/index.html')

@bp.route('/api/search')
@login_required
def search():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify([])
        
    products = Product.query.filter(
        Product.is_active == True,
        Product.stock_quantity > 0,
        (Product.name.ilike(f'%{query}%')) | 
        (Product.sku.ilike(f'%{query}%')) | 
        (Product.barcode.ilike(f'%{query}%'))
    ).limit(10).all()
    
    results = []
    for p in products:
        results.append({
            'id': p.id,
            'name': p.name,
            'price': float(p.selling_price),
            'stock': p.stock_quantity,
            'unit': p.unit
        })
    return jsonify(results)

@bp.route('/api/checkout', methods=['POST'])
@login_required
def checkout():
    data = request.get_json()
    if not data or not data.get('items'):
        return jsonify({'success': False, 'message': 'Cart is empty'})
        
    items = data['items']
    payment_method = data.get('payment_method', 'Cash')
    
    subtotal = 0
    
    try:
        invoice_num = f"INV-{datetime.now().strftime('%Y%m%d')}-{str(uuid.uuid4())[:6].upper()}"
        
        sale = Sale(
            invoice_number=invoice_num,
            user_id=current_user.id,
            payment_method=payment_method,
            subtotal=0,
            grand_total=0
        )
        db.session.add(sale)
        db.session.flush() 
        
        for item in items:
            product = Product.query.get(item['id'])
            if not product or not product.is_active:
                raise ValueError(f"Product {item['name']} is invalid or inactive.")
                
            qty = int(item['quantity'])
            if qty <= 0:
                raise ValueError("Quantity must be greater than zero.")
                
            if product.stock_quantity < qty:
                raise ValueError(f"Not enough stock for {product.name}. Only {product.stock_quantity} available.")
                
            line_total = float(product.selling_price) * qty
            subtotal += line_total
            
            sale_item = SaleItem(
                sale_id=sale.id,
                product_id=product.id,
                quantity=qty,
                unit_price=product.selling_price,
                line_total=line_total
            )
            db.session.add(sale_item)
            
            product.stock_quantity -= qty
            
            txn = InventoryTransaction(
                product_id=product.id,
                user_id=current_user.id,
                transaction_type='Sale',
                quantity_changed=-qty,
                reference_id=invoice_num
            )
            db.session.add(txn)
            
        sale.subtotal = subtotal
        sale.grand_total = subtotal 
        
        db.session.commit()
        return jsonify({'success': True, 'invoice_number': invoice_num})
        
    except ValueError as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': 'An unexpected error occurred.'})
