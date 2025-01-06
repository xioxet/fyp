from passlib.hash import pbkdf2_sha256 as sha256
import jwt

def generate_hash(password):
    return sha256.hash(password)

def verify_hash(hashed, password):
    return sha256.verify(password, hashed)

def create_jwt(data, secret_key):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, secret_key, algorithm='HS256')
    return encoded_jwt