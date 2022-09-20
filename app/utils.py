#This is a utils.py file that contains the utility code

from passlib.context import CryptContext                            #used to store user password in hash format
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")   #inform passlib to use bcrypt hashing algorithm

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)