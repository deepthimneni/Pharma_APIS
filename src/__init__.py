from flask import Flask
from .config import Config, Configdb
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .users.register_blueprint import register_blueprint
from .models.extensions import db

app = Flask(__name__)

app.config.from_object(Config)
app.config.from_object(Configdb)

#object creation
db.init_app(app)

from .models.User import User
from .models.Company import Company
from .models.Product import Product

app.register_blueprint(register_blueprint, url_prefix="/api/user")

with app.app_context():
    db.create_all()
    db.session.commit()


