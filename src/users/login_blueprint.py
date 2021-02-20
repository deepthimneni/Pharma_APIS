from flask import Blueprint, request, Response, jsonify
from src.models.User import User
from src.utils.Utils import generate_salt, generate_hash

login_authentication = Blueprint("login_authentication", __name__)

@login_authentication.route("/login", methods=["POST"])
def login_auth():
    user_name = request.json["user_name"]
    #http request, request content , json key value pairs, user_name is key, will the get value
    # admin = request.json["phone"]
    password = request.json["password"]
    if (len(user_name) != 0 and len(password) != 0) :
        record= User.query.filter(User.user_name == user_name).first()
        if (record):
            password_hash = generate_hash(password, record.password_salt)
            if (password_hash == record.password_hash):
                user_id = record.id
                jwt_token = generate_jwt_token({"id": user_id})
                return jsonify({"jwt_token": jwt_token})
            else:
                return  jsonify({"message": "Password incorrect"})
        else:
            return  jsonify({"message": "Users not found"})
    else:
        Response(status=400)

