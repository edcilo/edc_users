from fixture import app, auth, client
from helpers import getPermission
from ms.models import Permission
from ms.repositories import Repository


class PermissionRepository(Repository):
    def get_model(self):
        return Permission

class MockRepository(Repository):
    pass


def test_get_model(app):
    with app.app_context():
        MockRepository.__abstractmethods__ = set()
        mockRepo = MockRepository()
        model = mockRepo.get_model()
        assert model is None


def test_add(app):
    with app.app_context():
        mockRepo = PermissionRepository()
        model = mockRepo.add({"name": "foo"})
        assert isinstance(model, Permission)


def test_all(app):
    with app.app_context():
        mockRepo = PermissionRepository()
        items = mockRepo.all()
        assert len(items) > 0


def test_find(app):
    with app.app_context():
        model = getPermission("User - list")
        mockRepo = PermissionRepository()
        res = mockRepo.find(model.id)
        assert isinstance(res, Permission)


def test_find_by_attribute(app):
    with app.app_context():
        mockRepo = PermissionRepository()
        res = mockRepo.find_by_attr("name", "User - list", fail=False)
        assert isinstance(res, Permission)


def test_find_optional(app):
    with app.app_context():
        mockRepo = PermissionRepository()
        res = mockRepo.find_optional({"name": "User - list", "fixed": "bar"}, fail=False)
        assert isinstance(res, Permission)


def test_update(app):
    with app.app_context():
        model = getPermission("User - list")
        mockRepo = PermissionRepository()
        res = mockRepo.update("foo", {"name": "bar"}, fail=False)
        assert res is None
        res = mockRepo.update(model.id, {"name": "bar"}, fail=False)
        assert res.name == "bar"


def test_delete(app):
    with app.app_context():
        model = getPermission("User - list")
        mockRepo = PermissionRepository()
        res = mockRepo.delete("foo", fail=False)
        assert res is None
        res = mockRepo.delete(model.id, fail=False)
        assert res is not None
        res = mockRepo.find(model.id, fail=False)
        assert res is None
