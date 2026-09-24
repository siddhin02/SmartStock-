from flask import Blueprint, render_template, request
from flask_login import login_required
from app.models import Sale, SaleItem

bp = Blueprint('sales', __name__, url_prefix='/sales')

@bp.route('/')
@login_required
def index():
    query = Sale.query.order_by(Sale.created_at.desc())

    search = request.args.get('search', '').strip()
    payment = request.args.get('payment', '').strip()
    date_from = request.args.get('date_from', '').strip()
    date_to = request.args.get('date_to', '').strip()

    if search:
        query = query.filter(Sale.invoice_number.ilike(f'%{search}%'))
    if payment:
        query = query.filter(Sale.payment_method == payment)
    if date_from:
        query = query.filter(Sale.created_at >= date_from)
    if date_to:
        query = query.filter(Sale.created_at <= date_to + ' 23:59:59')

    sales = query.limit(200).all()
    return render_template('sales/index.html', sales=sales,
                           search=search, payment=payment,
                           date_from=date_from, date_to=date_to)

@bp.route('/<int:id>')
@login_required
def detail(id):
    sale = Sale.query.get_or_404(id)
    items = SaleItem.query.filter_by(sale_id=sale.id).all()
    return render_template('sales/detail.html', sale=sale, items=items)
