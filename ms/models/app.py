import datetime
import uuid
from ms.db import db
from .associationTables import app_permission_table, app_role_table


class App(db.Model):
    __tablename__ = 'app'

    _fillable = [
        'name',
        'description', ]

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    name = db.Column(
        db.String(length=255),
        nullable=False,
        unique=True)
    description = db.Column(
        db.String(length=255),
        nullable=True)
    token = db.Column(
        db.String(length=1024),
        nullable=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    permissions = db.relationship(
        "Permission",
        lazy="dynamic",
        secondary=app_permission_table,
        passive_deletes=True)
    roles = db.relationship(
        "Role",
        lazy="dynamic",
        secondary=app_role_table,
        passive_deletes=True)

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<App {self.id}>"

    @property
    def roles_permissions(self):
        permissions = list()
        roles = self.roles.all()
        for role in roles:
            permissions = list(set(permissions + role.permissions.all()))
        return permissions

    @property
    def all_permissions(self):
        permissions = self.permissions.all() or list()
        for p in self.roles_permissions:
            if p not in permissions:
                permissions.append(p)
        return permissions

    @property
    def roles_list(self):
        roles = self.roles.all()
        roles_list = list()
        for role in roles:
            roles_list.append(role.name)
        return roles_list
