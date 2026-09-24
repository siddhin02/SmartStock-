import pytest

from app import create_app
from app.extensions import db
from app.models import User


class TestConfig:
    TESTING = True
    SECRET_KEY = 'test-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


@pytest.fixture
def app():
    app = create_app(TestConfig)

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def user(app):
    user = User(
        username='testuser',
        role='Staff',
        is_active=True
    )
    user.set_password('TestPassword123')
    db.session.add(user)
    db.session.commit()
    return user

@pytest.fixture
def admin_user(app):
    user = User(
        username='adminuser',
        role='Admin',
        is_active=True
    )
    user.set_password('AdminPassword123')
    db.session.add(user)
    db.session.commit()
    return user
