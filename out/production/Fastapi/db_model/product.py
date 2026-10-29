
from sqlalchemy import *
from config.database import Base
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    description = Column(String)
    price = Column(Float,nullable=False)
    quantity = Column(String,nullable=False)

