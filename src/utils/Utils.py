import os
import jwt
from hashlib import pbkdf2_hmac
 
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

# password salt technique
def generate_salt():
    salt = os.urandom(16)
    return salt.hex()

# password hash technique
def generate_hash(plain_password, password_salt):
    password_hash = pbkdf2_hmac(
        "sha256",
        b"%b" % bytes(plain_password, "utf-8"),
        b"%b" % bytes(password_salt, "utf-8"),
        10000,
    )
    return password_hash.hex()

def generate_jwt_token(content):
    encoded_content = jwt.encode(content, JWT_SECRET_KEY, algorithm="HS256")
    token = str(encoded_content).split("'")[1]
    return token