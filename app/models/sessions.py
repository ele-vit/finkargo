from app import db

class SessionToken(db.Model):
    __tablename__ = "session_tokens"

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)