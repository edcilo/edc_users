from flask_wtf import FlaskForm
from ms.models import User
from ms.db import db


class UserRepository():
    model = None

    def __init__(self) -> None:
        self.model = User

    def form_to_dict(self, form: FlaskForm) -> dict:
        return {
            "username": form.username.data,
            "password": form.password.data,
            "email": form.email.data if hasattr(form, 'email') else None
        }

    def add(self, data: dict) -> User:
        user = self.model(**data)
        db.session.add(user)
        db.session.commit()
        return user

    def find(self, id: int) -> User:
        user = self.model.query.filter_by(id=id).first()
        return user

    def find_by_attr(self, column: str, value: str) -> User:
        user = self.model.query.filter_by(**{column: value}).first()
        return user


userRepo = UserRepository()
