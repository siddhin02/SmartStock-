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

    # We will register blueprints here in the future
    # from app.routes.auth import bp as auth_bp
    # app.register_blueprint(auth_bp, url_prefix='/auth')

    return app
