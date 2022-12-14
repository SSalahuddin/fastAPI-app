from fastapi import FastAPI                                    #import fastapi library
from fastapi import Response, status, HTTPException            #imports Response/status/HTTPException fastapi modules
from fastapi import Depends, APIRouter                         #import Depends/APIRouter fastapi modules
from typing import List                                        #to use List type in response model
from sqlalchemy.orm import Session
from ..import models, schemas, utils
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED,  response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_pwd = utils.hash(user.password)      #take the provided password and hash it
    user.password = hashed_pwd                  #update the password with the hashed one
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user  

@router.get("/{id}", response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):         
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,     
                             detail=f"user with {id} was not found")
    return user