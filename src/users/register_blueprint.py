from flask import Blueprint, request, Response, jsonify
from src.models.User import User
from src.utils.Utils import generate_salt, generate_hash

register_blueprint = Blueprint("register_blueprint", __name__) #blueprint creation

@register_blueprint.route("/register", methods=["POST"])
def register_user():
    data = request.get_json() #read data from request

    error_message = validate_user_input(data)

    if error_message :
        return Response(error_message, status = 400)
    else:
        user_record= User.query.filter(User.user_name == data["user_name"]).first()
        if user_record: return Response("User Name already exists", 400)

        password_salt = generate_salt()
        password_hash = generate_hash(data["password"], password_salt)
        new_user = User(user_name=data["user_name"],
                        shop_name=data["shop_name"],
                        drug_licence_1=data["drug_license_1"],
                        drug_licence_2=data["drug_license_2"],
                        gstr_number=data["gst_number"],
                        aadhar_pan_number=data["aadhar_pan"],
                        phone_number=data["phone"],
                        shop_address= data["address_shop"],
                        password_hash=password_hash,
                        password_salt=password_salt)
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        return Response(status=201)

def validate_user_input(data):
    if not(data["user_name"]):
        return "Please enter user name"
    elif not(data["password"]):
        return "Need to enter password"
    else:
        return ""