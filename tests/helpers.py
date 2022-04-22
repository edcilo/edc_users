from ms.models import Permission, Role, User
from ms.repositories import UserRepository
from ms.db import db


def getPermission(permission):
    return Permission.query.filter_by(name=permission).first()


def getRole(role):
    return Role.query.filter_by(name=role).first()


def getUser(email):
    return User.query.filter_by(email=email).first()


def saveUser(email, phone, password, role):
    userRepo = UserRepository()
    user = userRepo.add({
        "email": email,
        "phone": phone,
        "password": password,
        "role_id": role.id
    })
    return user
