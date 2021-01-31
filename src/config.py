import os 
from dotenv import load_dotenv

load_dotenv()


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object): 
    DEBUG = True
    CSRF_ENABLED = True #cross site request forgery

class Configdb(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI") #db connection string
    SQLALCHEMY_TRACK_MODIFICATIONS = False 