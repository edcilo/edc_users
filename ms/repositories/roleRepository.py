from sqlalchemy import or_
from ms.models import Role
from .permissionRepository import PermissionRepository
from .repository import Repository


class RoleRepository(Repository):
    def get_model(self):
        return Role

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

    def update(self, id, data, fail=True):
        role = self.find(id, fail=fail)
        success = False
        if role.name != "root":
            role.update(data)
            self.db_save(role)
            success = True
        return role, success

    # TODO: add form validator
    def sync_permissions(self, id, permissions):
        permissionRepo = PermissionRepository()
        role = self.find(id)
        role.permissions = list()
        for permission_id in permissions:
            permission = permissionRepo.find(permission_id)
            role.permissions.append(permission)
        self.db_save(role)

    def delete(self, id, fail=True):
        role = self.find(id, fail=fail)
        success = False
        if role.name != "root" and role.fixed == False:
            self.db_delete(role)
            success = True
        return role, success
