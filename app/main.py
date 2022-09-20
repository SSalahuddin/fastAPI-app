#This is a main.py file that creates fastapi application server

from fastapi import FastAPI                                    #import fastapi library
from fastapi.middleware.cors import CORSMiddleware             #to use CORS module of fastapi

from .import models
from .database import engine
from .routers import post, user, auth, vote
from .config import Settings
from app import database

app = FastAPI()

#CORS
# enable particular origins, methods, or header allowed
origins = ["*"]                 #list of all the domains that can talk to our API, "*" means PUBLIC API
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],        #allow specific http methods
    allow_headers=["*"],        #allow specific http headers
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")                                  
def root():                                     
    return {"message": "Python API v1.0!"}