import datetime
import uuid
from werkzeug.security import generate_password_hash, check_password_hash
from ms.db import db
from ms.models import Role


class User(db.Model):
    __tablename__ = 'users'

    _fillable = (
        'phone',
        'email',
        'role_id',
        'name',
        'lastname',
        'mothername',
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
    mothername = db.Column(db.String(50), nullable=True)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    role_id = db.Column(
        db.String(length=36),
        db.ForeignKey(Role.id, ondelete='CASCADE'),
        nullable=False)
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    role = db.relationship('Role', back_populates='users', lazy=False)

    def __init__(self, data: dict) -> None:
        self.setAttrs(data)

    def __repr__(self) -> str:
        return f"<User {self.id} {self.email}>"

    @property
    def fullname(self) -> str:
        return f'{self.name} {self.lastname}'

    def set_password(self, password: str) -> None:
        self.password = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
