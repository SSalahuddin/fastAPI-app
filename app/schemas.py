#This is a schemas.py file that defines the pydantic SCHEMA

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, conint             #to get data in a provided SCHEMA/basemodel

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserCreate(UserBase):
    pass

class User(BaseModel):
    id: int
    email: EmailStr
    created_At: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

#-------------------------------------------------------------------------------------------------------------------

class PostBase(BaseModel):
    title: str                                                 
    content: str                                                
    published: bool = True 

#class used to create and update a post
class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_At: datetime
    user_id: int                #for foreign key
    owner: User
    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: Post
    votes: int
    class Config:
        orm_mode = True

#-------------------------------------------------------------------------------------------------------------------

#this class will desging the token
class Token(BaseModel):
    access_token: str
    token_type: str

#this class will define the contents of token
class TokenData(BaseModel):
    id: Optional[str] = None        #token consists of id only and that can be optional too

#-------------------------------------------------------------------------------------------------------------------

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)
