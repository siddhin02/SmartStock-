from decimal import Decimal

from app.extensions import db
from app.models import Category, InventoryTransaction, Product


def login(client, username, password):
    return client.post(
        '/auth/login',
        data={
            'username': username,
            'password': password
        },
        follow_redirects=False
    )


def test_authenticated_user_can_view_products(client, user):
    login(client, 'testuser', 'TestPassword123')

    response = client.get('/products/')

    assert response.status_code == 200
    assert b'Products' in response.data


def test_staff_cannot_add_product(client, user):
    login(client, 'testuser', 'TestPassword123')

    response = client.get('/products/add', follow_redirects=True)

    assert response.status_code == 200
    assert b'Only administrators can add products.' in response.data


def test_admin_can_add_product(client, admin_user, app):
    category = Category(name='Test Category')
    db.session.add(category)
    db.session.commit()

    login(client, 'adminuser', 'AdminPassword123')

    response = client.post(
        '/products/add',
        data={
            'name': 'Test Product',
            'category_id': str(category.id),
            'sku': 'TEST-SKU-001',
            'barcode': 'TEST-BARCODE-001',
            'purchase_price': '100.00',
            'selling_price': '150.00',
            'stock_quantity': '10',
            'min_stock_level': '5',
            'unit': 'pcs'
        },
        follow_redirects=False
    )

    assert response.status_code == 302

    product = Product.query.filter_by(sku='TEST-SKU-001').first()

    assert product is not None
    assert product.name == 'Test Product'
    assert product.purchase_price == Decimal('100.00')
    assert product.selling_price == Decimal('150.00')
    assert product.stock_quantity == 10


def test_initial_stock_creates_stock_in_transaction(client, admin_user, app):
    category = Category(name='Stock Test Category')
    db.session.add(category)
    db.session.commit()

    login(client, 'adminuser', 'AdminPassword123')

    client.post(
        '/products/add',
        data={
            'name': 'Stock Test Product',
            'category_id': str(category.id),
            'sku': 'STOCK-SKU-001',
            'barcode': 'STOCK-BARCODE-001',
            'purchase_price': '50.00',
            'selling_price': '75.00',
            'stock_quantity': '12',
            'min_stock_level': '5',
            'unit': 'pcs'
        }
    )

    product = Product.query.filter_by(sku='STOCK-SKU-001').first()

    transaction = InventoryTransaction.query.filter_by(
        product_id=product.id,
        transaction_type='Stock-in'
    ).first()

    assert transaction is not None
    assert transaction.quantity_changed == 12
    assert transaction.reference_id == 'Initial Stock Creation'
    assert transaction.user_id == admin_user.id


def test_duplicate_sku_is_rejected(client, admin_user, app):
    category = Category(name='SKU Test Category')
    db.session.add(category)

    existing = Product(
        name='Existing Product',
        category=category,
        sku='DUPLICATE-SKU',
        purchase_price=Decimal('100.00'),
        selling_price=Decimal('150.00'),
        stock_quantity=0,
        min_stock_level=5,
        unit='pcs'
    )
    db.session.add(existing)
    db.session.commit()

    login(client, 'adminuser', 'AdminPassword123')

    response = client.post(
        '/products/add',
        data={
            'name': 'Another Product',
            'category_id': str(category.id),
            'sku': 'DUPLICATE-SKU',
            'barcode': 'NEW-BARCODE',
            'purchase_price': '80.00',
            'selling_price': '120.00',
            'stock_quantity': '0',
            'min_stock_level': '5',
            'unit': 'pcs'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'A product with this SKU already exists.' in response.data
    assert Product.query.filter_by(name='Another Product').first() is None


def test_duplicate_barcode_is_rejected(client, admin_user, app):
    category = Category(name='Barcode Test Category')
    db.session.add(category)

    existing = Product(
        name='Existing Barcode Product',
        category=category,
        barcode='DUPLICATE-BARCODE',
        purchase_price=Decimal('100.00'),
        selling_price=Decimal('150.00'),
        stock_quantity=0,
        min_stock_level=5,
        unit='pcs'
    )
    db.session.add(existing)
    db.session.commit()

    login(client, 'adminuser', 'AdminPassword123')

    response = client.post(
        '/products/add',
        data={
            'name': 'Another Barcode Product',
            'category_id': str(category.id),
            'sku': 'NEW-SKU',
            'barcode': 'DUPLICATE-BARCODE',
            'purchase_price': '80.00',
            'selling_price': '120.00',
            'stock_quantity': '0',
            'min_stock_level': '5',
            'unit': 'pcs'
        },
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b'A product with this Barcode already exists.' in response.data
    assert Product.query.filter_by(name='Another Barcode Product').first() is None
