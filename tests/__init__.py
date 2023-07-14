import jwt

from app import app
from app.utils.jwt import generate_token

headers = {
    "Authorization": "Basic " + generate_token(1)
}
