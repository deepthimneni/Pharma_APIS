from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from flask_apispec.extension import FlaskApiSpec
docs = FlaskApiSpec()

db = SQLAlchemy()

# ma = Marshmallow()