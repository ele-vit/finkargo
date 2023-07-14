from app import app
import datetime
import jwt

def generate_token(user_id):
    payload = {
        'user_id': str(user_id),
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
    }

    token = jwt.encode(payload, app.config['SECRET_KEY'])
    return token

def decode_token(token):
    data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    return data

