from ms.models import Permission
from sqlalchemy import or_
from .repository import Repository


class PermissionRepository(Repository):
    def get_model(self):
        return Permission

    def all(
            self,
            search=None,
            order_column='created_at',
            order='desc',
            paginate=False,
            page=1,
            per_page=15):
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        if search is not None:
            q = q.filter(or_(self._model.name.like(f'%{search}%')))
        q = q.order_by(order_by())
        return q.paginate(page, per_page=per_page) if paginate else q.all()

    def delete(self, id, fail=True):
        permission = self.find(id, fail=fail)
        success = False
        if not permission.fixed:
            self.db_delete(permission)
            success = True
        return permission, success
