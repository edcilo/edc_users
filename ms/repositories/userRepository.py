import uuid
from sqlalchemy import or_
from ms.db import db
from ms.models import User
from ms.repositories import Repository


class UserRepository(Repository):
    def activate(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(is_active=True)
        db.session.add(user)
        db.session.commit()
        return user

    def add(self, data: dict) -> User:
        user = self.model(**data)
        db.session.add(user)
        db.session.commit()
        return user

    def deactivate(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(is_active=False)
        db.session.add(user)
        db.session.commit()
        return user

    def delete(self, id: int, fail: bool = False) -> User:
        user = self.find(id, fail=fail, strict=False)
        db.session.delete(user)
        db.session.commit()
        return user

    def find(self, id: int, fail: bool = False, strict: bool = True) -> User:
        filters = {'id': id}
        if strict:
            filters['deleted'] = False
        q = self.model.query.filter_by(**filters)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_by_attr(self,
                     column: str,
                     value: str,
                     fail: bool = False,
                     strict: bool = True) -> User:
        q = self.model.query.filter_by(**{column: value})
        if strict:
            q = q.filter_by(deleted=False)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_or(self,
                filter: dict[str, str],
                fail: bool = False,
                strict: bool = True) -> User:
        filters = [
            getattr(
                self.model,
                key) == val for key,
            val in filter.items()]
        q = self.model.query.filter(or_(*filters))
        if strict:
            q = q.filter_by(deleted=False)
        user = q.first_or_404() if fail else q.first()
        return user

    def get_all(self,
                search=None,
                order_column: str = 'id',
                order: str = 'asc',
                paginate: bool = False,
                page: int = 1,
                per_page: int = 15,
                strict: bool = True):
        column = getattr(self.model, order_column)
        order_by = getattr(column, order)
        q = self.model.query
        if search is not None:
            q = q.filter(or_(self.model.phone.like(f'%{search}%'),
                             self.model.email.like(f'%{search}%')))
        if strict:
            q = q.filter_by(deleted=False)
        q = q.order_by(order_by())
        users = q.paginate(page, per_page=per_page) if paginate else q.all()
        return users

    def restore(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail, strict=False)
        user.update(deleted=False)
        db.session.add(user)
        db.session.commit()
        return user

    def soft_delete(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(deleted=True)
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, id: int, data: dict, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(**data)
        db.session.add(user)
        db.session.commit()
        return user


userRepo = UserRepository(User)
