from decimal import Decimal

from app.extensions import db
from app.models import Product, Sale, SaleItem


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


def test_empty_cart_rejected(client, user):
    login(client, 'testuser', 'TestPassword123')

    response = client.post(
        '/billing/api/checkout',
        json={
            'items': [],
            'payment_method': 'Cash'
        }
    )

    data = response.get_json()

    assert response.status_code == 200
    assert data['success'] is False
    assert data['message'] == 'Cart is empty'


def test_single_item_bill_calculation(client, user):
    product = create_product(
        'Billing Product',
        'BILL-SKU-001',
        '100.00',
        10
    )

    login(client, 'testuser', 'TestPassword123')

    response = client.post(
        '/billing/api/checkout',
        json={
            'items': [
                {
                    'id': product.id,
                    'name': product.name,
                    'quantity': 2
                }
            ],
            'payment_method': 'Cash'
        }
    )

    data = response.get_json()

    assert data['success'] is True

    sale = Sale.query.filter_by(
        invoice_number=data['invoice_number']
    ).first()

    assert sale is not None
    assert sale.subtotal == Decimal('200.00')
    assert sale.grand_total == Decimal('200.00')
    assert sale.payment_method == 'Cash'


def test_multiple_items_bill_calculation(client, user):
    product_one = create_product(
        'Product One',
        'BILL-SKU-002',
        '100.00',
        10
    )

    product_two = create_product(
        'Product Two',
        'BILL-SKU-003',
        '75.50',
        10
    )

    login(client, 'testuser', 'TestPassword123')

    response = client.post(
        '/billing/api/checkout',
        json={
            'items': [
                {
                    'id': product_one.id,
                    'name': product_one.name,
                    'quantity': 2
                },
                {
                    'id': product_two.id,
                    'name': product_two.name,
                    'quantity': 3
                }
            ],
            'payment_method': 'UPI'
        }
    )

    data = response.get_json()

    assert data['success'] is True

    sale = Sale.query.filter_by(
        invoice_number=data['invoice_number']
    ).first()

    assert sale is not None
    assert sale.subtotal == Decimal('426.50')
    assert sale.grand_total == Decimal('426.50')
    assert sale.payment_method == 'UPI'

    items = SaleItem.query.filter_by(sale_id=sale.id).all()

    assert len(items) == 2


def test_sale_item_line_total_is_calculated(client, user):
    product = create_product(
        'Line Total Product',
        'BILL-SKU-004',
        '125.25',
        10
    )

    login(client, 'testuser', 'TestPassword123')

    response = client.post(
        '/billing/api/checkout',
        json={
            'items': [
                {
                    'id': product.id,
                    'name': product.name,
                    'quantity': 4
                }
            ],
            'payment_method': 'Card'
        }
    )

    data = response.get_json()

    assert data['success'] is True

    sale = Sale.query.filter_by(
        invoice_number=data['invoice_number']
    ).first()

    sale_item = SaleItem.query.filter_by(
        sale_id=sale.id
    ).first()

    assert sale_item.quantity == 4
    assert sale_item.unit_price == Decimal('125.25')
    assert sale_item.line_total == Decimal('501.00')


def test_zero_quantity_rejected(client, user):
    product = create_product(
        'Zero Quantity Product',
        'BILL-SKU-005',
        '100.00',
        10
    )

    login(client, 'testuser', 'TestPassword123')

    response = client.post(
        '/billing/api/checkout',
        json={
            'items': [
                {
                    'id': product.id,
                    'name': product.name,
                    'quantity': 0
                }
            ],
            'payment_method': 'Cash'
        }
    )

    data = response.get_json()

    assert data['success'] is False
    assert data['message'] == 'Quantity must be greater than zero.'


def test_insufficient_stock_rejected(client, user):
    product = create_product(
        'Limited Stock Product',
        'BILL-SKU-006',
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
