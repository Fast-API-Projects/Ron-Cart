from sqlalchemy.orm import Session

from db_model.product import Product


def get_all_products(db: Session):
    return db.query(Product).all()


def create_products(db: Session, product: Product):
    db_product = Product(id=product.id,
                         name=product.name,
                         description=product.description,
                         price=product.price,
                         quantity=product.quantity)
    db.add(db_product)
    db.commit()
    return db_product


def update_product_repo(new_id: int, db: Session, name: str, description: str, price: float, quantity: int):
    filtered_product = db.query(Product).filter(Product.id == new_id).first()
    filtered_product.price = price
    filtered_product.description = description
    filtered_product.quantity = quantity
    filtered_product.name = name
    db.commit()
    db.refresh(filtered_product)
    return filtered_product


def delete_db_product(new_id: int, db: Session, product: Product):
    filtered_product = db.query(Product).filter(Product.id == new_id).first()
    db.delete(filtered_product)
    db.commit()
    return "Product successfully deleted"
