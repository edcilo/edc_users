from flask_wtf import FlaskForm
from ms.models import User
from ms.db import db


class UserRepository():
    model = None

    def __init__(self) -> None:
        self.model = User

    def form_to_dict(self, form: FlaskForm, cols: tuple) -> dict:
        data = dict()
        for c in cols:
            data[c] = getattr(form, c).data
        return data

    def add(self, data: dict) -> User:
        user = self.model(**data)
        db.session.add(user)
        db.session.commit()
        return user

    def find(self, id: int, fail: bool = False) -> User:
        q = self.model.query.filter_by(id=id)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_by_attr(self, column: str, value: str, fail: bool = False) -> User:
        q = self.model.query.filter_by(**{column: value})
        user = q.first_or_404() if fail else q.first()
        return user

    def update(self, id: int, data: dict, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(**data)
        db.session.add(user)
        db.session.commit()
        return user


userRepo = UserRepository()
