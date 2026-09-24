from flask import Blueprint, render_template, request, make_response
from flask_login import login_required
from app.models import Product, Sale, SaleItem, Category, InventoryTransaction
from app.extensions import db
from datetime import date, timedelta
from sqlalchemy import func

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/')
@login_required
def index():
    return render_template('reports/index.html')

@bp.route('/sales')
@login_required
def sales_report():
    # Default: today
    date_from = request.args.get('date_from') or date.today().isoformat()
    date_to = request.args.get('date_to') or date.today().isoformat()

    sales = Sale.query.filter(
        func.date(Sale.created_at) >= date_from,
        func.date(Sale.created_at) <= date_to,
        Sale.status == 'Completed'
    ).order_by(Sale.created_at.desc()).all()

    from decimal import Decimal
    total_revenue = sum(
        (s.grand_total or Decimal("0.00") for s in sales),
        Decimal("0.00")
    )
    total_bills = len(sales)

    # Payment method breakdown
    payment_summary = db.session.query(
        Sale.payment_method,
        func.count(Sale.id).label('count'),
        func.sum(Sale.grand_total).label('total')
    ).filter(
        func.date(Sale.created_at) >= date_from,
        func.date(Sale.created_at) <= date_to,
        Sale.status == 'Completed'
    ).group_by(Sale.payment_method).all()

    return render_template('reports/sales.html',
        sales=sales,
        total_revenue=total_revenue,
        total_bills=total_bills,
        payment_summary=payment_summary,
        date_from=date_from,
        date_to=date_to
    )

@bp.route('/low-stock')
@login_required
def low_stock():
    low = Product.query.filter(
        Product.is_active == True,
        Product.stock_quantity <= Product.min_stock_level
    ).order_by(Product.stock_quantity.asc()).all()

    return render_template('reports/low_stock.html', products=low)

@bp.route('/inventory-movements')
@login_required
def inventory_movements():
    # Default: today
    date_from = request.args.get('date_from') or date.today().isoformat()
    date_to = request.args.get('date_to') or date.today().isoformat()
    movement_type = request.args.get('movement_type') or 'All'

    query = InventoryTransaction.query.filter(
        func.date(InventoryTransaction.created_at) >= date_from,
        func.date(InventoryTransaction.created_at) <= date_to
    )

    if movement_type != 'All':
        query = query.filter(
            InventoryTransaction.transaction_type == movement_type
        )

    transactions = query.order_by(
        InventoryTransaction.created_at.desc()
    ).all()

    movement_types = [
        'Stock-in',
        'Stock-out',
        'Adjustment',
        'Sale'
    ]

    return render_template(
        'reports/inventory_movements.html',
        transactions=transactions,
        date_from=date_from,
        date_to=date_to,
        movement_type=movement_type,
        movement_types=movement_types
    )


@bp.route('/inventory')
@login_required
def inventory():
    products = Product.query.filter_by(is_active=True).order_by(Product.name).all()
    total_value = sum(float(p.purchase_price) * p.stock_quantity for p in products)
    return render_template('reports/inventory.html', products=products, total_value=total_value)



