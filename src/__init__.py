from flask import Flask
from .config import Config, Configdb
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .users.register_blueprint import register_blueprint
from .models.extensions import db, docs
from .products.products_blueprint import products_blueprint
from .company.company_blueprint import company_blueprint
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from .users.login_blueprint import login_authentication

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
app.config.from_object(Configdb)


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='pharma',
        version='v1',
        openapi_version = '2.0',
        plugins=[MarshmallowPlugin()],
    ),
    'APISPEC_SWAGGER_URL': '/api/swagger/',
    'APISPEC_SWAGGER_UI_URL': '/api/swagger-ui/'

})

#object creation
db.init_app(app)

from .models.User import User
from .models.Company import Company
from .models.Product import Product

#ma.init_app(app)

app.register_blueprint(register_blueprint, url_prefix="/api/user")
app.register_blueprint(products_blueprint, url_prefix="/api/products")
app.register_blueprint(company_blueprint, url_prefix="/api/company")
app.register_blueprint(login_blueprint, url_prefix="/api")

docs.init_app(app)

with app.app_context():
    db.create_all()
    db.session.commit()


