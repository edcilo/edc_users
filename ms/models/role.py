import datetime
import uuid
from ms.db import db


class Role(db.Model):
    __tablename__ = 'roles'

    _fillable = ('name')

    id = db.Column(
        db.String(length=36),
        default=lambda: str(uuid.uuid4()),
        primary_key=True)
    name = db.Column(db.String(50), unique=True)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    def __init__(self, data: dict) -> None:
        self.setAttrs(data)

    def __repr__(self) -> str:
        return f"<Role {self.id} {self.name}>"
