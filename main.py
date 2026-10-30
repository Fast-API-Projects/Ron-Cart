from fastapi import FastAPI

from config.database import Base, engine
from db_model.product import Product
from db_model.user import User
from controller.auth import router as auth_router
from controller.product_controller import router as product_router
from controller.user_controller import router as user_router

app = FastAPI(title="Ron Cart", description="vaango vandhu vaangitu pongo", version="1.0.0")

Base.metadata.create_all(bind=engine)

app.include_router(product_router)
app.include_router(user_router)
app.include_router(auth_router)
