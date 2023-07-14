from sqlalchemy.exc import IntegrityError
from app.utils.exceptions import MyCustomException
from app.utils.jwt import generate_token
from app import bcrypt
from app.repositories.user_repository import UserRepository
from pydantic import ValidationError


class UserService():
    def __init__(self, data, schema):
        self.user_repository = UserRepository()
        self.schema = schema
        self.user = data

    def create_user(self):
        try:
            user_schema = self.schema(**self.user)
            hashed_password = bcrypt.generate_password_hash(
                user_schema.password).decode('utf-8')
            user_schema.password = hashed_password
            created_user = self.user_repository.create(user_schema)
            return "User created successfully", 201
        except IntegrityError as e:
            return str(MyCustomException(str(e.orig.args[0]))), 409
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400

    def login(self):
        try:
            self.schema(**self.user)
            user = self.user_repository.find_user(
                self.user['email'], self.user['password'])
            if user:
                return generate_token(user.id), 201
            else:
                return str(MyCustomException("User not valid")), 401
        except IntegrityError as e:
            return str(MyCustomException(str(e.orig.args[0]))), 409
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400

    def get_user(self):
        try:
            usr_schema = self.schema(id=self.user)
            user = self.user_repository.get(usr_schema.id)
            if user:
                return user.to_dict(), 201
            else:
                return {"message": "User not found"}, 404
        except IntegrityError as e:
            return str(MyCustomException(str(e.orig.args[0]))), 409
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400

    def update_user(self):
        try:
            usr_schema = self.schema(**self.user)
            hashed_password = bcrypt.generate_password_hash(
                usr_schema.password).decode('utf-8')
            usr_schema.password = hashed_password
            response, status_code = self.user_repository.update(usr_schema)
            return response, status_code
        except IntegrityError as e:
            return str(MyCustomException(str(e.orig.args[0]))), 409
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400

    def delete_user(self):
        try:
            usr_schema = self.schema(id=self.user)
            response, status_code = self.user_repository.delete(usr_schema.id)
            return response, status_code
        except IntegrityError as e:
            return str(MyCustomException(str(e.orig.args[0]))), 409
        except ValidationError as e:
            errors = []
            for error in e.errors():
                errors.append(
                    {'field': error['loc'][0], 'message': error['msg']})
            return errors, 400
