from ms.models import Role, User
from ms.db import db


def getRole(role):
    return Role.query.filter_by(name=role).first()


def getUser(email):
    return User.query.filter_by(email=email).first()
