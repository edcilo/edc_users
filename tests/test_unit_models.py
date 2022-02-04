from fixture import app
from helpers import getRole
from ms.models import Role, User


def test_user(app):
    with app.app_context():
        role = getRole('client')
        user = User({
            'email': 'test@example.com',
            'phone': '1231231231',
            'name': 'jhon',
            'lastname': 'doe',
            'mothername': '',
            'role_id': role.id,
            'password': 'secret'
        })
        assert str(user) == f'<User {user.id} {user.email}>'
        assert user.email == 'test@example.com'
        assert user.fullname == 'jhon doe'
        assert user.password == None
        user.set_password('secret')
        assert user.password != None
        assert user.verify_password('secret') == True
        assert user.verify_password('secreto') == False


def test_role(app):
    with app.app_context():
        role = Role({'name': 'test'})
        assert str(role) == f'<Role {role.id} {role.name}>'
        assert role.name == 'test'
