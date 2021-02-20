from flask import Blueprint, request, Response, jsonify
from src.models.User import User
from src.utils.Utils import generate_salt, generate_hash
from flask_apispec import use_kwargs, marshal_with

register_blueprint = Blueprint("register_blueprint", __name__) #blueprint creation

@register_blueprint.route("/register", methods=("POST"))
@marshal_with(UserSchema(many=True))
@use_kwargs({'user_name': fields.Str(),  
            "shop_name":fields.Str(),
            "drug_licence_1":fields.Str(),
            "drug_licence_2":fields.Str(),
            "gst_number":fields.Str(),
            "aadhar_pan":fields.Str(),
            "phone":fields.Str(),
            "address_shop":fields.Str(),
            "password":fields.Str()})
def register_user(**kwargs):
    error_message = validate_user_input(kwargs)

    if error_message :
        return Response(error_message, status = 400)
    else:
        user_record= User.query.filter(User.user_name == kwargs.get("user_name")).first()
        if user_record: return Response("User Name already exists", 400)

        password_salt = generate_salt()
        password_hash = generate_hash(kwargs.get("password"), password_salt)
        new_user = User(user_name=kwargs.get("user_name"),
                        shop_name=kwargs.get("shop_name"),
                        drug_licence_1=kwargs.get("drug_license_1"),
                        drug_licence_2=kwargs.get("drug_license_2"),
                        gstr_number=kwargs.get("gst_number"),
                        aadhar_pan_number=kwargs.get("aadhar_pan"),
                        phone_number=kwargs.get("phone"),
                        shop_address= kwargs.get("address_shop"),
                        password_hash=password_hash,
                        password_salt=password_salt)
        db.session.add(new_user)  # Adds new User record to kwargs.getbase
        db.session.commit()  # Commits all changes
        return Response(status=201)

def validate_user_input(kwargs):
    if not(kwargs.get("user_name")):
        return "Please enter user name"
    elif not(kwargs.get("password")):
        return "Need to enter password"
    else:
        return ""
docs.register(get_users, blueprint=register_blueprint.name)
