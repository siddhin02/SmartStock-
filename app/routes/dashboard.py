from flask import Blueprint, render_template
from flask_login import login_required
from app.models import Product, Sale, SaleItem
from app.extensions import db
from datetime import datetime, date
from sqlalchemy import func

bp = Blueprint('dashboard', __name__)

@bp.route('/')
@bp.route('/dashboard')
@login_required
def index():
    today = date.today()
    month_start = today.replace(day=1)

    # Product stats
    total_products = Product.query.filter_by(is_active=True).count()
    low_stock = Product.query.filter(
        Product.is_active == True,
        Product.stock_quantity > 0,
        Product.stock_quantity <= Product.min_stock_level
    ).count()
    out_of_stock = Product.query.filter(
        Product.is_active == True,
        Product.stock_quantity == 0
    ).count()
    total_stock = db.session.query(func.sum(Product.stock_quantity)).filter_by(is_active=True).scalar() or 0

    # Sales stats
    today_sales = db.session.query(func.sum(Sale.grand_total)).filter(
        func.date(Sale.created_at) == today,
        Sale.status == 'Completed'
    ).scalar() or 0

    today_bills = Sale.query.filter(
        func.date(Sale.created_at) == today,
        Sale.status == 'Completed'
    ).count()

    monthly_sales = db.session.query(func.sum(Sale.grand_total)).filter(
        func.date(Sale.created_at) >= month_start,
        Sale.status == 'Completed'
    ).scalar() or 0

    # Recent 8 transactions
    recent_sales = Sale.query.order_by(Sale.created_at.desc()).limit(8).all()

    # Current month daily sales chart data
    from datetime import timedelta
    chart_labels = []
    chart_data = []

    current_day = month_start
    while current_day <= today:
        label = current_day.strftime('%d %b')
        total = db.session.query(func.sum(Sale.grand_total)).filter(
            func.date(Sale.created_at) == current_day,
            Sale.status == 'Completed'
        ).scalar() or 0

        chart_labels.append(label)
        chart_data.append(float(total))
        current_day += timedelta(days=1)

    return render_template('dashboard/index.html',
        total_products=total_products,
        low_stock=low_stock,
        out_of_stock=out_of_stock,
        total_stock=total_stock,
        today_sales=today_sales,
        today_bills=today_bills,
        monthly_sales=monthly_sales,
        recent_sales=recent_sales,
        chart_labels=chart_labels,
        chart_data=chart_data
    )

