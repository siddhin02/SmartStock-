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
