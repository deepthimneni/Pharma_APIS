from .extensions import db

class User(db.Model):
    __tablename__ = 'tbl_users'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(64), index=True, nullable= False)
    shop_name = db.Column(db.String(256))
    drug_licence_1 = db.Column(db.String(64))
    drug_licence_2 = db.Column(db.String(64))
    gstr_number = db.Column(db.String(64))
    aadhar_pan_number = db.Column(db.String(64))
    phone_number = db.Column(db.String(16))
    shop_address = db.Column(db.String(256))
    password_hash = db.Column(db.String(256), nullable= False)
    password_salt = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)

