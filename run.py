from app import create_app
from app.extensions import db
# Import models here so Alembic can detect them for migrations
from app.models import User, Category, Product, Customer, Sale, SaleItem, InventoryTransaction, ShopSettings

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db, 
        'User': User, 
        'Category': Category, 
        'Product': Product, 
        'Sale': Sale
    }

if __name__ == '__main__':
    app.run()

