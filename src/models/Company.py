from .extensions import db

class Company(db.Model):
    __tablename__ = 'tbl_company'
    __table_args__ = {'extend_existing': True} 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    company_name = db.Column(db.String(64), index=True, nullable= False)
    company_type = db.Column(db.String(64))

    def __repr__(self):
        return '<id {}>'.format(self.id)