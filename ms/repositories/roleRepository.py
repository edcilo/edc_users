import uuid
from flask_sqlalchemy import Pagination
from typing import Any, Union
from ms.models import Role
from .repository import Repository


class RoleRepository(Repository):
    def get_model(self) -> Role:
        return Role

    def add(self, data: dict) -> Role:
        role = self._model(data)
        self.db_save(role)
        return role

    def all(self, search: str = None,
            order_column: str = 'created_at',
            order: str = 'desc',
            paginate: bool = False,
            page: int = 1,
            per_page: int = 15) -> Union[list, Pagination]:
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        if search is not None:
            q = q.filter(self._model.name.like(f'%{search}%'))
        q = q.order_by(order_by())
        users = q.paginate(page, per_page=per_page) if paginate else q.all()
        return users

    def delete(self, id: uuid, fail: bool = False) -> Role:
        role = self.find(id, fail=fail)
        if len(role.users) == 0:
            self.db_delete(role)
            return role
        else:
            return None

    def find(self, id: str, fail: bool = False) -> Role:
        filters = {'id': id}
        q = self._model.query.filter_by(**filters)
        return q.first_or_404() if fail else q.first()

    def find_by_attr(self, column: str, value: str,
                     fail: bool = False) -> Role:
        q = self._model.query.filter_by(**{column: value})
        user = q.first_or_404() if fail else q.first()
        return user

    def update(self, id: int, data: dict, fail: bool = False) -> Role:
        role = self.find(id, fail=fail)
        role.update(data)
        self.db_save(role)
        return role
