from ms.models import User
from ms.db import db
from ms.repositories import Repository


class UserRepository(Repository):
    def add(self, data: dict) -> User:
        user = self.model(**data)
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, id: int, fail: bool = False) -> None:
        user = self.find(id, fail=fail)
        db.session.delete(user)
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


userRepo = UserRepository(User)
