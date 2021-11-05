import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from ms.db import db


class User(db.Model):
    __tablename__ = 'users'

    fillable = (
        'username',
        'email'
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

    def __init__(self, username: str, email: str, password: str) -> None:
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)

    def __repr__(self) -> str:
        return f"<User '{self.id}' '{self.username}'>"

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
