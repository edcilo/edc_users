import datetime
from flask import abort
from sqlalchemy import or_
from ms import app
from ms.models import User
from .permissionRepository import PermissionRepository
from .roleRepository import RoleRepository
from .repository import Repository


class UserRepository(Repository):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.roleRepo = RoleRepository()
        self.rootRole = "root"
        self.cache_key_prefix = "ms-users-"

    def get_model(self):
        return User

    def add(self, data):
        role_id = data.get("role_id") if "role_id" in data else self.roleRepo.find_by_attr(
            'name', self._model._default_role).id
        role = self.roleRepo.find(role_id)
        user = self._model(data)
        user.roles.append(role)
        if 'password' in data:
            user.set_password(data['password'])
        else:
            return None
        self.db_save(user)
        self.setCache(user)
        return user

    def all(
            self,
            search=None,
            order_column='created_at',
            order='desc',
            paginate=False,
            page=1,
            per_page=15,
            deleted=False):
        column = getattr(self._model, order_column)
        order_by = getattr(column, order)
        q = self._model.query
        if search is not None:
            q = q.filter(or_(self._model.id.like(f'%{search}%'),
                             self._model.email.like(f'%{search}%'),
                             self._model.phone.like(f'%{search}%'),
                             self._model.name.like(f'%{search}%'),
                             self._model.lastname.like(f'%{search}%')))
        if not deleted:
            q = q.filter(self._model.deleted_at.is_(None))
        else:
            q = q.filter(self._model.deleted_at.is_not(None))
        q = q.order_by(order_by())
        return q.paginate(page, per_page=per_page) if paginate else q.all()

    def find(self, id, fail=True, with_deleted=False):
        filters = {'id': id}
        if not with_deleted:
            filters['deleted_at'] = None
        q = self._model.query.filter_by(**filters)
        return q.first_or_404() if fail else q.first()

    def find_by_attr(self, column, value, fail=True, with_deleted=False):
        q = self._model.query.filter_by(**{column: value})
        if not with_deleted:
            q = q.filter(self._model.deleted_at.is_(None))
        return q.first_or_404() if fail else q.first()

    def find_optional(self, filter, fail=True, with_deleted=False):
        filters = [
            getattr(self._model, key) == val for key, val in filter.items()
        ]
        q = self._model.query.filter(or_(*filters))
        if not with_deleted:
            q = q.filter(self._model.deleted_at.is_(None))
        return q.first_or_404() if fail else q.first()

    def update_password(self, id, password, fail=True) -> User:
        user = self.find(id, fail)
        if user is not None:
            user.set_password(password)
            self.db_save(user)
        return user

    def sync_permissions(self, id, permissions):
        permissionRepo = PermissionRepository()
        user = self.find(id)
        user.permissions = list()
        for permission_id in permissions:
            permission = permissionRepo.find(permission_id)
            user.permissions.append(permission)
        self.db_save(user)
        self.setCache(user)

    def sync_roles(self, id, roles):
        roleRepo = RoleRepository()
        user = self.find(id)
        user.roles = list()
        for role_id in roles:
            role = roleRepo.find(role_id)
            user.roles.append(role)
        self.db_save(user)
        self.setCache(user)

    def activate(self, id, fail=True):
        user = self.find(id, fail=fail)
        if user is not None and not user.is_active:
            user.is_active = True
            self.db_save(user)
        return user

    def deactivate(self, id, fail=True):
        user = self.find(id, fail=fail)
        if user is not None and user.is_active:
            user.is_active = False
            self.db_save(user)
        return user

    def soft_delete(self, id, fail=True):
        user = self.find(id, fail=fail)
        if user is not None and user.deleted_at is None:
            self.canBeDeleted(user)
            user.deleted_at = datetime.datetime.now()
            self.db_save(user)
            self.deleteCache(user)
        return user

    def restore(self, id, fail=True):
        user = self.find(id, fail=fail, with_deleted=True)
        if user is not None and user.deleted_at is not None:
            user.deleted_at = None
            self.db_save(user)
            self.setCache(user)
        return user

    def delete(self, id, fail=True):
        user = self.find(id, fail=fail, with_deleted=True)
        if user is not None:
            self.canBeDeleted(user)
            user.permissions = list()
            user.roles = list()
            self.db_delete(user)
            self.deleteCache(user)
        return user

    def canBeDeleted(self, user):
        if self.rootRole in user.roles_list:
            abort(403)

    def updateCache(self) -> bool:
        users = self.all()
        app.cache.truncate(self.cache_key_prefix)
        for user in users:
            self.setCache(user)
        return True

    def setCache(self, user):
        permissions = [p.name for p in user.all_permissions]
        data = {
            "id": user.id,
            "email": user.email,
            "permissions": permissions,
            "roles": user.roles_list
        }
        app.cache.set(f"{self.cache_key_prefix}{user.id}", data)

    def deleteCache(self, user):
        app.cache.delete(f"{self.cache_key_prefix}{user.id}")
