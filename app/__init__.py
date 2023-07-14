from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import SQLALCHEMY_DATABASE_URI, SECRET_KEY
from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.config.from_object("config")

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False #INDAGAR
app.config["SECRET_KEY"] = SECRET_KEY

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controllers import (
    matrix,
    financial_statements,
    user_manager,
    auth,
)