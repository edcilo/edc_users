from ms.helpers.jwt import jwtHelper
from ms.models import Role, User
from ms.db import db


def getRole(role):
    roles = Role.query.all()
    role = Role.query.filter_by(name=role).first()
    db.session.close()
    return role


def createUser(data):
    user = User(data)
    if 'password' in data:
        user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return user


def getUser(email):
    user = User.query.filter_by(email=email).first()
    db.session.close()
    return user


def createJhonDoe():
    role = getRole('client')
    jhonDoe = getUser('jhon.doe@example.com')
    if jhonDoe:
        return jhonDoe
    return createUser({
        'phone': '1231231231',
        'email': 'jhon.doe@example.com',
        'password': 'secret',
        'role_id': role.id
    })


def createJWT(payload):
    return jwtHelper.get_tokens(payload)
