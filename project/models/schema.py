from datetime import datetime
from project import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    secret = db.Column(db.String(50), nullable=False)
    is_delete = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __init__(self, email: str, password: str, secret: str, is_delete: int):
        self.email = email
        self.password = password
        self.secret = secret
        self.is_delete = is_delete

    def __repr__(self):
        return f"{self.email}"


class CommentModel(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(50), nullable=False)
    is_delete = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    modified_at = db.Column(db.DateTime, nullable=False, default=datetime.now())
    created_by = db.Column(db.Integer, nullable=False)
    modified_by = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.message}, {self.created_by}"
