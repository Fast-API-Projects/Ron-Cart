from fastapi import Depends
from fastapi import FastAPI, APIRouter
from sqlalchemy.orm import Session

from config.database import get_db
from repositories.product_repo import get_all_products, create_products, update_product_repo, delete_db_product
from schema.product import Product, UpdateProduct

app = FastAPI()

# product.Base.metadata.create_all(bind=engine)

router = APIRouter(prefix="/product_cart", tags=["products"])


@app.get("/")
def greet():
    return "Welcome"


# products=[Product(id=1, name="phone", description="budget phone", price=99,quantity= 10),
# Product(id=2,name= "laptop", description="gaming laptop",price= 999,quantity=8),
# Product(id=4,name= "airpod", description="buds",price= 988,quantity=6)]

@router.get("/product")
def get_all(db: Session = Depends(get_db)):
    return get_all_products(db)


@router.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    return create_products(db, product)


@router.put("/product")
def update_product(new_id: int, product: UpdateProduct, db: Session = Depends(get_db)):
    return update_product_repo(new_id, db, name=product.name, description=product.description,
                               quantity=product.quantity, price=product.price)


@router.post("/delete")
def delete_product(new_id: int, product: Product, db: Session = Depends(get_db)):
    return delete_db_product(new_id, db, product)

# @app.get("/products/{id}")
# def get_product(id : int):
#     for product in products:
#         if product.id==id:
#             return product
#     return "prod not found"

# @app.post("/product")
# def add_product(Product:Product):
#     products.append(Product)
#     return products

# @app.put("/product")
# def update(id:int,Product:Product):
#     for i in range(len(products)):
#         if products[i].id==id:
#             products[i]=Product
#             return "Added successfully"
#     return "No product found"

# @app.delete("/product")
# def delete_product(id:int):
#     for product in products:
#         if product.id==id:
#             products.remove(product)
#             return "Deleted successfully"
#     return "No product found"
