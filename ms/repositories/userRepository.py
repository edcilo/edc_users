import uuid
from typing import Any
from sqlalchemy import or_
from ms.models import User
from .repository import Repository


class UserRepository(Repository):
    def get_model(self) -> User:
        return User

    def activate(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.is_active = True
        self.db_save(user)
        return user

    def add(self, data: dict) -> User:
        user = self._model(data)
        if 'password' in data:
            user.set_password(data['password'])
        self.db_save(user)
        return user

    def deactivate(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.is_active = False
        self.db_save(user)
        return user

    def delete(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail, with_deleted=True)
        self.db_delete(user)
        return user

    def find(self, id: str, fail: bool = False,
             with_deleted: bool = False) -> User:
        filters: dict[str, Any] = {'id': id, 'deleted': with_deleted}
        q = self._model.query.filter_by(**filters)
        user = q.first_or_404() if fail else q.first()
        user = q.first()
        return user

    def find_by_attr(self, column: str, value: str, fail: bool = False,
                     with_deleted: bool = False) -> User:
        q = self._model.query.filter_by(**{column: value})
        q = q.filter_by(deleted=with_deleted)
        user = q.first_or_404() if fail else q.first()
        return user

    def find_optional(self, filter: dict, fail: bool = False,
                      with_deleted: bool = False) -> User:
        filters = [
            getattr(
                self._model,
                key) == val for key,
            val in filter.items()]
        q = self._model.query.filter(or_(*filters))
        q = q.filter_by(deleted=False)
        user = q.first_or_404() if fail else q.first()
        return user

    def all(self, search: str = None,
            order_column: str = 'id',
            order: str = 'desc',
            paginate: bool = False,
            page: int = 1,
            per_page: int = 15,
            with_deleted: bool = False):
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        if search is not None:
            q = q.filter(or_(self._model.email.like(f'%{search}%'),
                             self._model.phone.like(f'%{search}%')))
        q.filter_by(deleted=False)
        q = q.order_by(order_by())
        users = q.paginate(page, per_page=per_page) if paginate else q.all()
        return users

    def restore(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail, with_deleted=True)
        user.deleted = False
        self.db_save(user)
        return user

    def soft_delete(self, id: uuid, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.deleted = True
        self.db_save(user)
        return user

    def update(self, id: int, data: dict, fail: bool = False) -> User:
        user = self.find(id, fail=fail)
        user.update(data)
        self.db_save(user)
        return user
