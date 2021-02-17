from .extensions import db#, ma
from marshmallow_sqlalchemy import SQLAlchemySchema, ModelSchema
from src.models.extensions import db,docs

class Company(db.Model):
    __tablename__ = 'tbl_company'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(64), index=True, nullable= False)
    company_type = db.Column(db.String(64))

    def __repr__(self):
        return '<id {}>'.format(self.id)
    
class CompanySchema(SQLAlchemySchema):
    class Meta(SQLAlchemySchema.Meta):
        fields = ("id", "company_name", "company_type")
        model = Company
        sqla_session = db.session