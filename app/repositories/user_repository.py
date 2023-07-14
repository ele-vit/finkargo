from app import db
from app.models.user import User
from app import bcrypt
from sqlalchemy.exc import SQLAlchemyError

class UserRepository:
    def create(self, user_data):
        user = User(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password
        )
        db.session.add(user)
        db.session.commit()
        return user

    def get(self, user_id):
        return User.query.get(user_id)
    
    def find_user(self, email, password):
        user = db.session.query(User).filter(User.email == email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        return None

    def update(self, data):
        try:
            result = (
                db.session.query(User)
                .filter(User.id == int(data.id))
                .update(data.dict(), synchronize_session=False)
            )
            db.session.commit()
            msg, s_code = (
                ("Updated user successfully", 201)
                if result > 0
                else
                ("User not found", 404)
            )
            return {"message":msg}, s_code
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": str(e.orig.args[0])}, 400

    def delete(self, user_id):
        try:
            result = (
                db.session.query(User)
                .filter(User.id == int(user_id))
                .delete(synchronize_session=False)
            )
            db.session.commit()
            msg, s_code = (
                ("Deleted user successfully", 201)
                if result > 0
                else
                ("User not found", 404)
            )
            return {"message":msg}, s_code
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"message": str(e.orig.args[0])}, 400
        # user = User.query.get(user_id)
        # if user:
        #     db.session.delete(user)
        #     db.session.commit()
        #     return True # INDAGAR UN SOLO QUERY PARA ELIMINAR
        # else:
        #     return False
