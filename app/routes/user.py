from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import User
from app.extensions import db

bp = Blueprint('user', __name__, url_prefix='/users')


@bp.route('/')
@login_required
def index():
    if current_user.role != 'Admin':
        flash('Only administrators can access user management.', 'danger')
        return redirect(url_for('dashboard.index'))

    users = User.query.order_by(User.username).all()
    return render_template('user/index.html', users=users)


@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if current_user.role != 'Admin':
        flash('Only administrators can create users.', 'danger')
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '')
        confirm_password = request.form.get('confirm_password', '')

        if not username:
            flash('Username is required.', 'danger')
            return redirect(url_for('user.create'))

        if not password:
            flash('Password is required.', 'danger')
            return redirect(url_for('user.create'))

        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return redirect(url_for('user.create'))

        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('user.create'))

        user = User(
            username=username,
            role='Staff',
            is_active=True
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        flash('Staff user created successfully.', 'success')
        return redirect(url_for('user.index'))

    return render_template('user/create.html')

@bp.route('/<int:user_id>/toggle-status', methods=['POST'])
@login_required
def toggle_status(user_id):
    if current_user.role != 'Admin':
        flash('Only administrators can change user status.', 'danger')
        return redirect(url_for('dashboard.index'))

    user = User.query.get_or_404(user_id)

    if user.id == current_user.id:
        flash('You cannot change your own account status.', 'danger')
        return redirect(url_for('user.index'))

    user.is_active = not user.is_active
    db.session.commit()

    status = 'activated' if user.is_active else 'deactivated'
    flash(f'User "{user.username}" has been {status}.', 'success')

    return redirect(url_for('user.index'))