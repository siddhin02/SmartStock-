from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Customer, Sale
from app.extensions import db

bp = Blueprint('customer', __name__, url_prefix='/customers')

@bp.route('/')
@login_required
def index():
    search = request.args.get('search', '').strip()
    query = Customer.query.order_by(Customer.name)
    if search:
        query = query.filter(
            (Customer.name.ilike(f'%{search}%')) |
            (Customer.mobile.ilike(f'%{search}%'))
        )
    customers = query.all()
    return render_template('customer/index.html', customers=customers, search=search)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    if request.method == 'POST':
        name = request.form.get('name').strip()
        mobile = request.form.get('mobile').strip() or None
        email = request.form.get('email').strip() or None
        address = request.form.get('address').strip() or None

        if mobile and Customer.query.filter_by(mobile=mobile).first():
            flash('A customer with this mobile number already exists.', 'warning')
            return redirect(url_for('customer.add'))

        customer = Customer(name=name, mobile=mobile, email=email, address=address)
        db.session.add(customer)
        db.session.commit()
        flash(f'Customer "{name}" added successfully!', 'success')
        return redirect(url_for('customer.index'))

    return render_template('customer/add.html')

@bp.route('/<int:id>')
@login_required
def detail(id):
    customer = Customer.query.get_or_404(id)
    sales = Sale.query.filter_by(customer_id=id).order_by(Sale.created_at.desc()).all()
    return render_template('customer/detail.html', customer=customer, sales=sales)
