from flask import Flask
from .config import Config, Configdb
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .users.register_blueprint import register_blueprint
from .models.extensions import db#, ma
from .products.products_blueprint import products_blueprint
from .company.company_blueprint import company_blueprint


app = Flask(__name__)

app.config.from_object(Config)
app.config.from_object(Configdb)

#object creation
db.init_app(app)

from .models.User import User
from .models.Company import Company
from .models.Product import Product

#ma.init_app(app)

app.register_blueprint(register_blueprint, url_prefix="/api/user")
app.register_blueprint(products_blueprint, url_prefix="/api/products")
app.register_blueprint(company_blueprint, url_prefix="/api/company")

with app.app_context():
    db.create_all()
    db.session.commit()


