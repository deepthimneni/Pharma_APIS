from .extensions import db

class Product(db.Model):
    __tablename__ = 'tbl_products'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(64), index=True, nullable= False)
    power = db.Column(db.Integer,nullable=False)
    quantity = db.Column(db.Integer,nullable=False)
    company_id = db.Column(db.Integer,db.ForeignKey('tbl_company.id',ondelete='CASCADE'),nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)