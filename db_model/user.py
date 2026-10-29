from sqlalchemy import *

from config.database import Base


class User(Base):
    __tablename__ = "user"
    name = Column(String)
    mail = Column(String, primary_key=True)
    phno = Column(String(10), nullable=False)
    password = Column(String, nullable=False)
    role = Column(String(30), default="CUSTOMER", nullable=False)
