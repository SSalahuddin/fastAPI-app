#This is a config.py file that specifies all of our environment varaibles

from pydantic import BaseSettings

class Settings(BaseSettings):                   #Settings class
    database_hostname: str
    database_port: str
    database_name: str
    database_username: str
    database_password: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: int

    class Config:                               #Config subclass
        env_file = ".env"                       #path of .env file   

settings = Settings()                           #object/instance of Settings class
