from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Product, InventoryTransaction
from app.extensions import db

bp = Blueprint('inventory', __name__, url_prefix='/inventory')

@bp.route('/')
@login_required
def index():
    transactions = InventoryTransaction.query.order_by(InventoryTransaction.created_at.desc()).limit(100).all()
    return render_template('inventory/index.html', transactions=transactions)

@bp.route('/adjust/<int:product_id>', methods=['GET', 'POST'])
@login_required
def adjust(product_id):
    if current_user.role != 'Admin':
        flash('Only administrators can adjust stock manually.', 'danger')
        return redirect(url_for('product.index'))
        
    product = Product.query.get_or_404(product_id)
    
    if request.method == 'POST':
        adj_type = request.form.get('type') 
        quantity = request.form.get('quantity', type=int)
        reference = request.form.get('reference').strip()
        
        if not quantity or quantity <= 0:
            flash('Quantity must be greater than zero.', 'danger')
            return redirect(url_for('inventory.adjust', product_id=product.id))
            
        if adj_type in ['Stock-out', 'Adjustment (Remove)'] and product.stock_quantity < quantity:
            flash(f'Cannot remove {quantity}. Only {product.stock_quantity} available.', 'danger')
            return redirect(url_for('inventory.adjust', product_id=product.id))
            
        if adj_type in ['Stock-in', 'Adjustment (Add)']:
            product.stock_quantity += quantity
            actual_type = 'Stock-in' if adj_type == 'Stock-in' else 'Adjustment'
            q_changed = quantity
        else:
            product.stock_quantity -= quantity
            actual_type = 'Stock-out' if adj_type == 'Stock-out' else 'Adjustment'
            q_changed = -quantity
            
        txn = InventoryTransaction(
            product_id=product.id,
            user_id=current_user.id,
            transaction_type=actual_type,
            quantity_changed=q_changed,
            reference_id=reference if reference else 'Manual Adjustment'
        )
        
        db.session.add(txn)
        db.session.commit()
        
        flash(f'Stock updated for {product.name}. New stock: {product.stock_quantity}', 'success')
        return redirect(url_for('product.index'))
        
    return render_template('inventory/adjust.html', product=product)
