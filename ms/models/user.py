import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from ms.db import db
from .associationTables import user_permission_table, user_role_table


class User(db.Model):
    __tablename__ = 'user'

    _default_role = 'shopper'

    _fillable = (
        'phone',
        'email',
        'name',
        'lastname',
        'second_lastname',
    )

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    name = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=True)
    second_lastname = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    deleted_at = db.Column(
        db.DateTime,
        default=None,
        nullable=True
    )
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    profile = db.relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all,delete",
    )
    permissions = db.relationship(
        "Permission",
        lazy='dynamic',
        secondary=user_permission_table,
        passive_deletes=True)
    roles = db.relationship(
        "Role",
        lazy='dynamic',
        secondary=user_role_table,
        passive_deletes=True)

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self):
        return f"<User {self.id} {self.email}>"

    @property
    def fullname(self) -> str:
        return f'{self.name} {self.lastname} {self.second_lastname}'

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)

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
