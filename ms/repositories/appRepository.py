from sqlalchemy import or_
from ms.models import App
from .repository import Repository
from .permissionRepository import PermissionRepository
from .roleRepository import RoleRepository


class AppRepository(Repository):
    def get_model(self):
        return App

    def all(self,
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
            q = q.filter(or_(self._model.name.like(f'%{search}%'),
                             self._model.description.like(f'%{search}%')))
        q = q.order_by(order_by())
        return q.paginate(page, per_page=per_page) if paginate else q.all()

    def sync_permissions(self, id, permissions):
        permissionRepo = PermissionRepository()
        app = self.find(id)
        app.permissions = list()
        for permission_id in permissions:
            permission = permissionRepo.find(permission_id)
            app.permissions.append(permission)
        self.db_save(app)

    def sync_roles(self, id, roles):
        roleRepo = RoleRepository()
        app = self.find(id)
        app.roles = list()
        for role_id in roles:
            role = roleRepo.find(role_id)
            app.roles.append(role)
        self.db_save(app)
