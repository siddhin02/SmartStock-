from app.extensions import db
from app.models import User


def test_login_page_loads(client):
    response = client.get('/auth/login')

    assert response.status_code == 200


def test_valid_login(client, user):
    response = client.post(
        '/auth/login',
        data={
            'username': 'testuser',
            'password': 'TestPassword123'
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']


def test_invalid_credentials_rejected(client, user):
    response = client.post(
        '/auth/login',
        data={
            'username': 'testuser',
            'password': 'WrongPassword'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Invalid username or password.' in response.data


def test_inactive_user_cannot_login(client, user):
    user.is_active = False
    db.session.commit()

    response = client.post(
        '/auth/login',
        data={
            'username': 'testuser',
            'password': 'TestPassword123'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Your account is inactive.' in response.data


def test_authenticated_user_redirected_from_login(client, user):
    client.post(
        '/auth/login',
        data={
            'username': 'testuser',
            'password': 'TestPassword123'
        }
    )

    response = client.get('/auth/login', follow_redirects=False)

    assert response.status_code == 302
    assert '/dashboard' in response.headers['Location']


def test_logout(client, user):
    client.post(
        '/auth/login',
        data={
            'username': 'testuser',
            'password': 'TestPassword123'
        }
    )

    response = client.get('/auth/logout', follow_redirects=False)

    assert response.status_code == 302
    assert '/auth/login' in response.headers['Location']

def test_register_page_loads(client):
    response = client.get('/auth/register')

    assert response.status_code == 200


def test_user_can_register(client, app):
    response = client.post(
        '/auth/register',
        data={
            'username': 'newuser',
            'password': 'NewPassword123',
            'confirm_password': 'NewPassword123'
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert '/auth/login' in response.headers['Location']

    with app.app_context():
        registered_user = User.query.filter_by(username='newuser').first()

        assert registered_user is not None
        assert registered_user.password_hash != 'NewPassword123'
        assert registered_user.check_password('NewPassword123')


def test_duplicate_username_rejected(client, user):
    response = client.post(
        '/auth/register',
        data={
            'username': 'testuser',
            'password': 'NewPassword123',
            'confirm_password': 'NewPassword123'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Username already exists.' in response.data


def test_registration_password_mismatch_rejected(client):
    response = client.post(
        '/auth/register',
        data={
            'username': 'newuser',
            'password': 'NewPassword123',
            'confirm_password': 'DifferentPassword123'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'Passwords do not match.' in response.data

def test_registered_user_can_login(client, app):
    register_response = client.post(
        '/auth/register',
        data={
            'username': 'loginuser',
            'password': 'LoginPassword123',
            'confirm_password': 'LoginPassword123'
        },
        follow_redirects=False
    )

    assert register_response.status_code == 302
    assert '/auth/login' in register_response.headers['Location']

    login_response = client.post(
        '/auth/login',
        data={
            'username': 'loginuser',
            'password': 'LoginPassword123'
        },
        follow_redirects=False
    )

    assert login_response.status_code == 302
    assert '/dashboard' in login_response.headers['Location']


def test_admin_can_create_staff_user(client, admin_user, app):
    client.post(
        '/auth/login',
        data={
            'username': 'adminuser',
            'password': 'AdminPassword123'
        }
    )

    response = client.post(
        '/users/create',
        data={
            'username': 'staffcreated',
            'password': 'StaffPassword123',
            'confirm_password': 'StaffPassword123'
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert '/users/' in response.headers['Location']

    with app.app_context():
        staff_user = User.query.filter_by(username='staffcreated').first()

        assert staff_user is not None
        assert staff_user.role == 'Staff'
        assert staff_user.is_active is True
        assert staff_user.password_hash != 'StaffPassword123'
        assert staff_user.check_password('StaffPassword123')


def test_staff_cannot_create_user(client, user):
    client.post(
        '/auth/login',
        data={
            'username': 'testuser',
            'password': 'TestPassword123'
        }
    )

    response = client.post(
        '/users/create',
        data={
            'username': 'blockeduser',
            'password': 'BlockedPassword123',
            'confirm_password': 'BlockedPassword123'
        },
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/dashboard')
