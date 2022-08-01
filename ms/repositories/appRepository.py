from sqlalchemy import or_
from ms import app as ms_app
from ms.models import App
from .repository import Repository
from .permissionRepository import PermissionRepository
from .roleRepository import RoleRepository


class AppRepository(Repository):
    def __init__(self) -> None:
        super().__init__()
        self.cache_key_prefix = "ms-users-"

    def get_model(self):
        return App

    def add(self, data):
        app = super().add(data)
        self.setCache(app)
        return app

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

    def update_token(self, app, token):
        app = app if isinstance(app, App) else self.find(app)
        app.token = token
        self.db_save(app)
        self.setCache(app)
        return app

    def sync_permissions(self, id, permissions):
        permissionRepo = PermissionRepository()
        app = self.find(id)
        app.permissions = list()
        for permission_id in permissions:
            permission = permissionRepo.find(permission_id)
            app.permissions.append(permission)
        self.db_save(app)
        self.setCache(app)

    def sync_roles(self, id, roles):
        roleRepo = RoleRepository()
        app = self.find(id)
        app.roles = list()
        for role_id in roles:
            role = roleRepo.find(role_id)
            app.roles.append(role)
        self.db_save(app)
        self.setCache(app)

    def delete(self, id):
        app = super().delete(id)
        self.deleteCache(app)

    def setCache(self, app):
        permissions = [p.name for p in app.all_permissions]
        data = {
            "id": app.id,
            "name": app.name,
            "permissions": permissions,
            "roles": app.roles_list
        }
        ms_app.cache.set(f"{self.cache_key_prefix}{app.id}", data)

    def deleteCache(self, app):
        ms_app.cache.delete(f"{self.cache_key_prefix}{app.id}")
