from typing import Any
from ms.models import Role
from .repository import Repository


class RoleRepository(Repository):
    def get_model(self) -> Role:
        return Role

    def find(self, id: str, fail: bool = False) -> Role:
        filters = {'id': id}
        q = self._model.query.filter_by(**filters)
        return q.first_or_404() if fail else q.first()

    def find_by_attr(self, column: str, value: str,
                     fail: bool = False) -> Role:
        q = self._model.query.filter_by(**{column: value})
        user = q.first_or_404() if fail else q.first()
        return user
