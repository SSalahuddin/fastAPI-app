#This is a models.py file that uses Object-Relational Mapper (ORM) i.e. SQLALCHEMY

from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class Post(Base):
    __tablename__ = "postsORM"

    id = Column(Integer, primary_key=True, nullable=False)              #primary key
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_At = Column(TIMESTAMP(timezone=True), server_default=text('Now()'), nullable=False)
    
    #Foreign key with on delete set
    user_id = Column(Integer, ForeignKey("usersORM.id", ondelete="CASCADE"), nullable=False)  

    #Relataionship
    owner = relationship("User")

class User(Base):
    __tablename__ = "usersORM"

    id = Column(Integer, primary_key=True, nullable=False)                  #primary key
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)    
    created_At = Column(TIMESTAMP(timezone=True), server_default=text('Now()'), nullable=False)
    phone_number = Column(String, nullable=True)

class Vote(Base):
    __tablename__ = "votesORM"

    #Foreign keys with on delete set
    user_id = Column(Integer, ForeignKey("usersORM.id", ondelete="CASCADE"), primary_key=True)  #primary key 1
    post_id = Column(Integer, ForeignKey("postsORM.id", ondelete="CASCADE"), primary_key=True)  #primary key 2