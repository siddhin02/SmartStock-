def login(client, username, password):
    return client.post(
        '/auth/login',
        data={
            'username': username,
            'password': password
        },
        follow_redirects=False
    )


def test_staff_cannot_access_add_product(client, user):
    login(client, 'testuser', 'TestPassword123')

    response = client.get(
        '/products/add',
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/products/')


def test_admin_can_access_add_product(client, admin_user):
    login(client, 'adminuser', 'AdminPassword123')

    response = client.get(
        '/products/add',
        follow_redirects=False
    )

    assert response.status_code == 200
    assert b'Save Product' in response.data


def test_staff_cannot_access_user_management(client, user):
    login(client, 'testuser', 'TestPassword123')

    response = client.get(
        '/users/',
        follow_redirects=False
    )

    assert response.status_code == 302
    assert response.headers['Location'].endswith('/dashboard')


def test_admin_can_access_user_management(client, admin_user):
    login(client, 'adminuser', 'AdminPassword123')

    response = client.get(
        '/users/',
        follow_redirects=False
    )

    assert response.status_code == 200
    assert b'User Management' in response.data