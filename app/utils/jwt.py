from app import app
import jwt

def generate_token(user_id):
    token = jwt.encode({'user_id': str(user_id)}, app.config['SECRET_KEY'])
    return token

def decode_token(token):
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    return data

