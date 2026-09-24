from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Category
from app.extensions import db

bp = Blueprint('category', __name__, url_prefix='/categories')

@bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'POST':
        if current_user.role != 'Admin':
            flash('Only administrators can modify categories.', 'danger')
            return redirect(url_for('category.index'))
            
        name = request.form.get('name').strip()
        if name:
            existing = Category.query.filter_by(name=name).first()
            if existing:
                flash(f'Category "{name}" already exists.', 'warning')
            else:
                new_category = Category(name=name)
                db.session.add(new_category)
                db.session.commit()
                flash(f'Category "{name}" added successfully!', 'success')
        return redirect(url_for('category.index'))
        
    categories = Category.query.order_by(Category.name).all()
    return render_template('category/index.html', categories=categories)

@bp.route('/<int:id>/toggle')
@login_required
def toggle_active(id):
    if current_user.role != 'Admin':
        flash('Only administrators can modify categories.', 'danger')
        return redirect(url_for('category.index'))
        
    category = Category.query.get_or_404(id)
    category.is_active = not category.is_active
    db.session.commit()
    
    status = 'activated' if category.is_active else 'deactivated'
    flash(f'Category "{category.name}" has been {status}.', 'success')
    return redirect(url_for('category.index'))
