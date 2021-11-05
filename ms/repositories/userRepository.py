from sqlalchemy import or_
from ms.db import db
from ms.models import User
from ms.repositories import Repository


class UserRepository(Repository):
    def add(self, data: dict) -> User:
        user = self.model(**data)
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, id: int, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        db.session.delete(user)
        db.session.commit()
        return user

    def find(self, id: int, fail: bool = False) -> User:
        q = self.model.query.filter_by(id=id)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_by_attr(self,
                     column: str,
                     value: str,
                     fail: bool = False) -> User:
        q = self.model.query.filter_by(**{column: value})
        user = q.first_or_404() if fail else q.first()
        return user

    def get_all(self,
                search=None,
                order_column: str = 'id',
                order: str = 'asc',
                paginate: bool = False,
                page: int = 1,
                per_page: int = 15):
        column = getattr(self.model, order_column)
        order_by = getattr(column, order)
        q = self.model.query
        if search is not None:
            q = q.filter(or_(self.model.username.like(f'%{search}%'),
                             self.model.email.like(f'%{search}%')))
        q = q.order_by(order_by())
        users = q.paginate(page, per_page=per_page) if paginate else q.all()
        return users

    def update(self, id: int, data: dict, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(**data)
        db.session.add(user)
        db.session.commit()
        return user


userRepo = UserRepository(User)
