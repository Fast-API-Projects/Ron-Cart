from sqlalchemy import *  
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

db_url = "postgresql+psycopg2://postgres:2212@postgresql:5432/ron_cart"

engine = create_engine(db_url,echo=True)

Session = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()



def get_db():
    db=Session()
    #we need to close the session later
    try:
        yield db
    finally:
        db.close()