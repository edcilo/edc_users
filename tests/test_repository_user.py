from fixture import app, auth, client
from helpers import getPermission, getRole, getUser, saveUser
from ms.models import User
from ms.repositories import UserRepository


def test_check_model(app):
    with app.app_context():
        userRepo = UserRepository()
        model = userRepo.get_model()
        assert model == User


def test_add(app):
    with app.app_context():
        role = getRole('user')
        userRepo = UserRepository()
        user = userRepo.add({
            'email': 'jhon.doe@example.com',
            'phone': '1231231231',
            'role_id': role.id, })
        assert user is None
        user = userRepo.add({
            'email': 'jhon.doe@example.com',
            'phone': '1231231231',
            'password': 'secret',
            'role_id': role.id, })
        assert isinstance(user, User)
        assert user.id is not None
        assert user.password is not None


def test_all(app):
    with app.app_context():
        userRepo = UserRepository()
        users = userRepo.all()
        assert isinstance(users, list)
        assert len(users) == 9
        results = userRepo.all('shopper')
        assert len(results) == 1
        results = userRepo.all('foo')
        assert len(results) == 0


def test_find(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        userRepo = UserRepository()
        user_found = userRepo.find(user.id, fail=False)
        assert isinstance(user_found, User)
        user_not_found = userRepo.find('foo', fail=False)
        assert user_not_found is None


def test_find_by_attr(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        userRepo = UserRepository()
        user_found = userRepo.find_by_attr('email', 'jhon@example.com')
        assert isinstance(user_found, User)
        userRepo.soft_delete(user_found.id)
        user_found = userRepo.find_by_attr('email', 'jhon@example.com', with_deleted=True)
        assert user_found is not None


def test_find_optional(app):
    with app.app_context():
        userrole = getRole("user")
        saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        userRepo = UserRepository()
        user_found = userRepo.find_optional({
            'phone': 'invalidphone',
            'email': 'invalidemail'}, fail=False, with_deleted=True)
        assert user_found is None
        user_found = userRepo.find_optional({
            'phone': 'invalidphone',
            'email': 'jhon@example.com'}, fail=False, with_deleted=False)
        assert isinstance(user_found, User)
        assert user_found.email == 'jhon@example.com'


def test_update(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        user = getUser('jhon@example.com')
        userRepo = UserRepository()
        user_updated = userRepo.update(user.id, {'phone': '3213213213'})
        assert user_updated.phone == '3213213213'


def test_update_password(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        userRepo = UserRepository()

        model = userRepo.update_password("foo", 'secret2', fail=False)
        assert model is None

        old_password = user.password
        user_updated = userRepo.update_password(user.id, 'secret2')

        assert old_password != user_updated.password
        assert not user.verify_password('secret1')
        assert user.verify_password('secret2')


def test_sync_permissions(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        permission = getPermission("User - list")
        permissions = [permission.id]
        userRepo = UserRepository()
        assert user.permissions.count() == 0
        userRepo.sync_permissions(user.id, permissions)
        assert user.permissions.count() == 1
        userRepo.sync_permissions(user.id, [])
        assert user.permissions.count() == 0


def test_sync_roles(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        rootrole = getRole("root")
        userrole = getRole("user")
        roles = [rootrole.id]
        userRepo = UserRepository()
        assert user.roles.count() == 1
        userRepo.sync_roles(user.id, roles)
        assert user.roles.count() == 1


def test_activate_deactivate(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        userRepo = UserRepository()

        model = userRepo.activate("foo", fail=False)
        assert model is None
        model = userRepo.deactivate("foo", fail=False)
        assert model is None

        assert user.is_active == False
        user = userRepo.activate(user.id, fail=False)
        assert user.is_active == True
        user = userRepo.deactivate(user.id, fail=False)
        assert user.is_active == False


def test_soft_delete_restore(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)
        userRepo = UserRepository()

        model = userRepo.soft_delete("foo", fail=False)
        assert model is None
        model = userRepo.restore("foo", fail=False)
        assert model is None

        user = userRepo.soft_delete(user.id)
        assert user.deleted_at is not None
        user = userRepo.restore(user.id)
        assert user.deleted_at is None


def test_delete(app):
    with app.app_context():
        userrole = getRole("user")
        user = saveUser(email="jhon@example.com", phone="9879879871", password="secret", role=userrole)

        userRepo = UserRepository()
        userRepo.delete(user.id)
        user = userRepo.find(user.id, fail=False)
        assert user is None
