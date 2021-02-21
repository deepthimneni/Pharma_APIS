from flask_sqlalchemy import SQLAlchemy
# from flask_marshmallow import Marshmallow
from flask_apispec.extension import FlaskApiSpec
from marshmallow_sqlalchemy import SQLAlchemySchema
from webargs import fields

docs = FlaskApiSpec()

db = SQLAlchemy()

# ma = Marshmallow()
class ErrorSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        error_msg = fields.Str()

class LoginSchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        jwt_token = fields.Str()