from sqlalchemy.orm import Session
from app.config.database import SessionLocal
from app.models.product import Product

def populate_db():
    db: Session = SessionLocal()
    products = [
        {"name": "Laptop", "description": "A high-performance laptop.", "price": 999.99},
        {"name": "Smartphone", "description": "A latest-gen smartphone.", "price": 699.99},
        {"name": "Headphones", "description": "Noise-cancelling headphones.", "price": 199.99},
        {"name": "Monitor", "description": "A 4K ultra-wide monitor.", "price": 349.99},
        {"name": "Keyboard", "description": "A mechanical keyboard.", "price": 99.99},
    ]

    for product_data in products:
        product = Product(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"]
        )
        db.add(product)

    db.commit()
    db.close()
    print("Database populated successfully.")

if __name__ == "__main__":
    populate_db()
