import datetime
import uuid
from ms.db import db
from .associationTables import permission_role_table


class Role(db.Model):
    __tablename__ = 'role'

    _fillable = ('name', 'fixed',)

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    name = db.Column(
        db.String(length=120),
        unique=True,
        nullable=False)
    fixed = db.Column(
        db.Boolean,
        default=True,
        nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    permissions = db.relationship(
        "Permission",
        lazy='dynamic',
        secondary=permission_role_table)

    def __init__(self, data=None):
        if data is not None:
            self.setAttrs(data)

    def __repr__(self) -> str:
        return f"<Role {self.id} {self.name}>"
