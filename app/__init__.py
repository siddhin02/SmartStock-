from flask import Flask
from config import Config
from app.extensions import db, migrate, login_manager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message_category = 'info'

    from app.routes.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    from app.routes.dashboard import bp as dashboard_bp
    app.register_blueprint(dashboard_bp)
    
    from app.routes.category import bp as category_bp
    app.register_blueprint(category_bp)

    from app.routes.product import bp as product_bp
    app.register_blueprint(product_bp)

    from app.routes.inventory import bp as inventory_bp
    app.register_blueprint(inventory_bp)

    from app.routes.billing import bp as billing_bp
    app.register_blueprint(billing_bp)

    from app.routes.sales import bp as sales_bp
    app.register_blueprint(sales_bp)

    from app.routes.customer import bp as customer_bp
    app.register_blueprint(customer_bp)

    from app.routes.reports import bp as reports_bp
    app.register_blueprint(reports_bp)

    from app.routes.user import bp as user_bp
    app.register_blueprint(user_bp)

    @app.context_processor
    def inject_now():
        from datetime import datetime
        return {'now': datetime.now()}

    return app