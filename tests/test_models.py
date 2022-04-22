from ms.db import Model
from ms.models import Permission, Role, User


def test_model():
    mock = Model()
    mock._fillable = ["foo"]
    mock.setAttrs({"foo": "bar", "zoo": False})
    assert mock.foo == "bar"
    assert getattr(mock, "zoo", None) is None
    mock.update({"foo": "zoo"})
    assert mock.foo == "zoo"


def test_permission():
    permission = Permission()
    assert permission.name == None
    assert permission.fixed == None
    permission = Permission({
        'name': 'foo',
        'fixed': False,
    })
    assert str(permission) == f'<Permission {permission.id} {permission.name}>'
    assert permission.name == 'foo'
    assert permission.fixed == False


def test_role():
    role = Role()
    assert role.name == None
    assert role.fixed == None
    role = Role({
        'name': 'foo',
        'fixed': False,
    })
    assert str(role) == f'<Role {role.id} {role.name}>'
    assert role.name == 'foo'
    assert role.fixed == False


def test_user():
    user = User()
    assert user.email == None
    assert user.phone == None
    assert user.password == None
    user = User({
        'email': 'jhon.doe@example',
        'phone': '1231231231',
        'name': 'jhon',
        'lastname': 'doe',
        'mothername': 'foo'
    })
    assert str(user) == f'<User {user.id} {user.email}>'
    assert user.email == 'jhon.doe@example'
    assert user.phone == '1231231231'
    assert user.fullname == 'jhon doe foo'
