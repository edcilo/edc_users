from fixture import app
from helpers import getRole
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
        role = roleRepo.add({'name': 'test'})
        assert isinstance(role, Role)
        assert role.id is not None


def test_find(app):
    with app.app_context():
        role = getRole('client')
        roleRepo = RoleRepository()
        role_found = roleRepo.find(role.id)
        assert isinstance(role_found, Role)
        role_not_found = roleRepo.find('foo')
        assert role_not_found is None


def test_find_by_attribute(app):
    with app.app_context():
        roleRepo = RoleRepository()
        role_found = roleRepo.find_by_attr('name', 'client')
        assert isinstance(role_found, Role)

        role_found = roleRepo.find_by_attr('name', 'foo')
        assert role_found is None


def test_all(app):
    with app.app_context():
        roleRepo = RoleRepository()
        roles = roleRepo.all()
        assert isinstance(roles, list)
        assert len(roles) == 3
        results = roleRepo.all('client')
        assert len(results) == 1
        results = roleRepo.all('foo')
        assert len(results) == 0


def test_update(app):
    with app.app_context():
        role = getRole('client')
        roleRepo = RoleRepository()
        role_updated = roleRepo.update(role.id, {'name': 'test'})
        assert role_updated.name == 'test'


def test_delete(app):
    with app.app_context():
        role_client = getRole('client')
        roleRepo = RoleRepository()

        role_test = roleRepo.add({'name': 'test'})
        roleRepo.delete(role_test.id)
        role_test = roleRepo.find(role_test.id)
        assert role_test is None

        roleRepo.delete(role_client.id)
        role_client = roleRepo.find(role_client.id)
        assert role_client is not None
