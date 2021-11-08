import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from werkzeug.security import generate_password_hash, check_password_hash
from ms.db import db


class User(db.Model):
    __tablename__ = 'users'

    # TODO: implement fillable
    fillable = (
        'phone',
        'email',
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
    deleted = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(
        db.DateTime,
        default=datetime.datetime.utcnow,
        nullable=False)

    def __init__(
            self,
            email: str,
            phone: str,
            password: str,
            name: str = None,
            lastname: str = None,
            mothername: str = None) -> None:
        self.phone = phone
        self.email = email
        self.password = generate_password_hash(password)
        self.name = name
        self.lastname = lastname
        self.mothername = mothername

    def __repr__(self) -> str:
        return f"<User '{self.id}' '{self.email}'>"

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password, password)
