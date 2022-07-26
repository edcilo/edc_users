from fixture import app, auth, client
from helpers import getPermission
from ms.models import Permission
from ms.repositories import PermissionRepository


def test_check_model(app):
    with app.app_context():
        permissionRepo = PermissionRepository()
        model = permissionRepo.get_model()
        assert model == Permission


def test_add(app):
    with app.app_context():
        permissionRepo = PermissionRepository()
        permission = permissionRepo.add({
            'name': 'foo',
            'fixed': False, })
        assert isinstance(permission, Permission)
        assert permission.id is not None
        assert permission.fixed == False


def test_all(app):
    with app.app_context():
        permissionRepo = PermissionRepository()
        permissions = permissionRepo.all()
        assert isinstance(permissions, list)
        assert len(permissions) == 22
        results = permissionRepo.all('list')
        assert len(results) == 2
        results = permissionRepo.all('foo')
        assert len(results) == 0


def test_find(app):
    with app.app_context():
        permission = getPermission("User - list")
        permissionRepo = PermissionRepository()
        permission_found = permissionRepo.find(permission.id, fail=False)
        assert isinstance(permission_found, Permission)
        permission_not_found = permissionRepo.find('foo', fail=False)
        assert permission_not_found is None


def test_find_by_attr(app):
    with app.app_context():
        permissionRepo = PermissionRepository()
        permission_found = permissionRepo.find_by_attr('name', 'User - list', fail=False)
        assert isinstance(permission_found, Permission)
        permission_found = permissionRepo.find_by_attr('name', 'foo', fail=False)
        assert permission_found is None


def test_find_optional(app):
    with app.app_context():
        permissionRepo = PermissionRepository()
        permission_found = permissionRepo.find_optional({
            'name': 'User - list',
            'fixed': "foo"})
        assert isinstance(permission_found, Permission)
        assert permission_found.name == 'User - list'


def test_update(app):
    with app.app_context():
        permission = getPermission('User - list')
        permissionRepo = PermissionRepository()
        permission_updated = permissionRepo.update(permission.id, {'name': 'foo'})
        assert permission_updated.name == 'foo'


def test_delete(app):
    with app.app_context():
        permissionRepo = PermissionRepository()
        permission = getPermission('User - list')

        permission, success = permissionRepo.delete(permission.id)
        assert success == False
        permissionRepo.update(permission.id, {'fixed': False})
        permission, success = permissionRepo.delete(permission.id)
        assert success == True
        permission = permissionRepo.find(permission.id, fail=False)
        assert permission is None
