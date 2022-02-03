from fixture import app
from helpers import getRole, getUser
from ms.models import User
from ms.repositories import UserRepository


def test_check_model(app):
    with app.app_context():
        userRepo = UserRepository()
        model = userRepo.get_model()
        assert model == User


def test_add(app):
    with app.app_context():
        role = getRole('client')
        userRepo = UserRepository()
        user = userRepo.add({
            'username': 'jhon.doe',
            'email': 'jhon.doe@example.com',
            'phone': '1231231231',
            'password': 'secret',
            'role_id': role.id, })
        assert isinstance(user, User)
        assert user.id is not None
        assert user.password is not None


def test_activate_deactivate(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()

        assert user.is_active == False
        user = userRepo.activate(user.id, fail=True)
        assert user.is_active == True
        user = userRepo.deactivate(user.id, fail=True)
        assert user.is_active == False


def test_find(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()
        user_found = userRepo.find(user.id)
        assert isinstance(user_found, User)
        user_not_found = userRepo.find('foo')
        assert user_not_found is None


def test_find_by_attribute(app):
    with app.app_context():
        userRepo = UserRepository()
        user_found = userRepo.find_by_attr('email', 'client@example.com')
        assert isinstance(user_found, User)
        userRepo.soft_delete(user_found.id)
        user_found = userRepo.find_by_attr('email', 'client@example.com', with_deleted=True)
        assert user_found is not None


def test_find_optional(app):
    with app.app_context():
        userRepo = UserRepository()
        user_found = userRepo.find_optional({
            'phone': 'invalidphone',
            'email': 'client@example.com'})
        assert isinstance(user_found, User)
        assert user_found.email == 'client@example.com'


def test_all(app):
    with app.app_context():
        userRepo = UserRepository()
        users = userRepo.all()
        assert isinstance(users, list)
        assert len(users) == 8
        results = userRepo.all('client')
        assert len(results) == 1
        results = userRepo.all('foo')
        assert len(results) == 0


def test_update(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()
        user_updated = userRepo.update(user.id, {'phone': '3213213213'})
        assert user_updated.phone == '3213213213'


def test_update_password(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()

        old_password = user.password
        user_updated = userRepo.update_password(user.id, 'secret2')

        assert old_password != user_updated.password
        assert not user.verify_password('secret1')
        assert user.verify_password('secret2')


def test_soft_delete(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()
        user = userRepo.soft_delete(user.id)
        assert user.deleted == True


def test_restore(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()
        user = userRepo.restore(user.id)
        assert user.deleted == False


def test_delete(app):
    with app.app_context():
        user = getUser('client@example.com')
        userRepo = UserRepository()
        userRepo.delete(user.id)
        user = userRepo.find(user.id)
        assert user is None
