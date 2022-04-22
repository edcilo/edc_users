from fixture import app, auth, client
from helpers import getPermission, getRole
from ms.models import Role
from ms.repositories import RoleRepository


def test_check_model(app):
    with app.app_context():
        roleRepo = RoleRepository()
        model = roleRepo.get_model()
        assert model == Role


def test_add(app):
    with app.app_context():
        roleRepo = RoleRepository()
        role = roleRepo.add({
            'name': 'foo',
            'fixed': False, })
        assert isinstance(role, Role)
        assert role.id is not None
        assert role.fixed == False


def test_all(app):
    with app.app_context():
        roleRepo = RoleRepository()
        roles = roleRepo.all()
        assert isinstance(roles, list)
        assert len(roles) == 3
        results = roleRepo.all('root')
        assert len(results) == 1
        results = roleRepo.all('foo')
        assert len(results) == 0


def test_find(app):
    with app.app_context():
        roleRepo = RoleRepository()
        role = getRole("user")
        role_found = roleRepo.find(role.id, fail=False)
        assert isinstance(role_found, Role)
        role_not_found = roleRepo.find('foo', fail=False)
        assert role_not_found is None


def test_find_by_attr(app):
    with app.app_context():
        roleRepo = RoleRepository()
        role_found = roleRepo.find_by_attr('name', 'user', fail=False)
        assert isinstance(role_found, Role)
        role_found = roleRepo.find_by_attr('name', 'foo', fail=False)
        assert role_found is None


def test_find_optional(app):
    with app.app_context():
        roleRepo = RoleRepository()
        role_found = roleRepo.find_optional({
            'name': 'user',
            'fixed': "foo"})
        assert isinstance(role_found, Role)
        assert role_found.name == 'user'


def test_update(app):
    with app.app_context():
        role = getRole('user')
        roleRepo = RoleRepository()
        role_updated, success = roleRepo.update(role.id, {'name': 'foo'})
        assert role_updated.name == 'foo'


def test_sync_permissions(app):
    with app.app_context():
        permission = getPermission('User - list')
        role = getRole('user')
        roleRepo = RoleRepository()
        assert role.permissions.count() == 0
        roleRepo.sync_permissions(role.id, [permission.id])
        assert role.permissions.count() == 1


def test_delete(app):
    with app.app_context():
        roleRepo = RoleRepository()
        role = getRole('user')

        role, success = roleRepo.delete(role.id)
        assert success == False
        roleRepo.update(role.id, {'fixed': False})
        role, success = roleRepo.delete(role.id)
        assert success == True
        role = roleRepo.find(role.id, fail=False)
        assert role is None
