#This is a database.py file that uses Object-Relational Mapper (ORM) i.e. SQLALCHEMY 

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

#connection url
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

#sqlalchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#session instance handles the specified database 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#creates a new "Base" class from which all mapped classes should inherit
Base = declarative_base()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()