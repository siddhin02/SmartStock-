from decimal import Decimal

from app.extensions import db
from app.models import Product, InventoryTransaction


def login(client, username, password):
    return client.post(
        '/auth/login',
        data={
            'username': username,
            'password': password
        },
        follow_redirects=False
    )


def create_product(name, sku, price, stock):
    product = Product(
        name=name,
        sku=sku,
        purchase_price=Decimal('50.00'),
        selling_price=Decimal(str(price)),
        stock_quantity=stock,
        min_stock_level=5,
        unit='pcs',
        is_active=True
    )
    db.session.add(product)
    db.session.commit()
    return product


def test_negative_stock_prevented(client, user):
    product = create_product(
        'Negative Stock Product',
        'NEG-STOCK-001',
        '100.00',
        2
    )

    login(client, 'testuser', 'TestPassword123')

    response = client.post(
        '/billing/api/checkout',
        json={
            'items': [
                {
                    'id': product.id,
                    'name': product.name,
                    'quantity': 3
                }
            ],
            'payment_method': 'Cash'
        }
    )

    data = response.get_json()

    assert data['success'] is False
    assert 'Not enough stock' in data['message']

    db.session.refresh(product)

    assert product.stock_quantity == 2

    transaction = InventoryTransaction.query.filter_by(
        product_id=product.id,
        transaction_type='Sale'
    ).first()

    assert transaction is None
