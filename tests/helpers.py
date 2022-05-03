from typing import Any, Union
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


class RedisWrapper():
    def __init__(self) -> None:
        self.data = {}

    def set(self, key: str, val: str, ex: Union[int, None]=None) -> bool:
        self.data[key] = val
        return True

    def get(self, key: str) -> Any:
        return self.data.get(key, None)

    def delete(self, *args: str) -> int:
        c = 0
        for key in args:
            if key in self.data:
                del self.data[key]
                c += 1
        return c

    def exists(self, key:str) -> bool:
        return key in self.data

    def scan(self, cursor, match, count):
        keys = self.data.keys()
        return len(keys), keys

    def ping(self) -> bool:
        return True
