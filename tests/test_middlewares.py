from flask import request
from fixture import app, auth, client
from helpers import getPermission, getRole, getUser, saveUser
from ms.helpers.jwt import JwtHelper
from ms.middlewares.middleware import Middleware, middleware
from ms.middlewares import PermissionMiddleware, RoleMiddleware, permissionMiddleware, roleMiddleware
from ms.repositories import UserRepository


def test_middleware():
    class MockMiddleware(Middleware):
        def handler(self, request):
            return True

    @middleware(MockMiddleware)
    def mockFnc():
        return True

    assert Middleware.handler(Middleware, request) == None
    assert mockFnc() == True
    assert MockMiddleware().handler(request) == True


def test_permision_middleware(app):
    with app.app_context():
        rootRole = getRole("root")
        userRole = getRole("user")

        root = saveUser("jhon+00@example.com", "1231231230", "secret", rootRole)
        user = saveUser("jhon+01@example.com", "1231231231", "secret", userRole)

        permission = getPermission("User - list")
        userRepo = UserRepository()
        userRepo.sync_permissions(user.id, [permission.id])

        class RequestMock:
            auth = {"user": None}

        requestMock = RequestMock()
        permissionMiddleware = PermissionMiddleware(["User - list"])

        requestMock.auth["user"] = root
        res = permissionMiddleware.handler(requestMock)
        assert res == True

        requestMock.auth["user"] = user
        res = permissionMiddleware.handler(requestMock)
        assert res == True

        try:
            permissionMiddleware = PermissionMiddleware(["foo"])
            res = permissionMiddleware.handler(requestMock)
            assert False
        except:
            assert True


def test_role_middleware(app):
    with app.app_context():
        rootRole = getRole("root")
        userRole = getRole("user")

        root = saveUser("jhon+00@example.com", "1231231230", "secret", rootRole)
        user = saveUser("jhon+01@example.com", "1231231231", "secret", userRole)

        class RequestMock:
            auth = {"user": None}

        requestMock = RequestMock()
        roleMiddleware = RoleMiddleware(["user"])

        requestMock.auth["user"] = root
        res = roleMiddleware.handler(requestMock)
        assert res == True

        requestMock.auth["user"] = user
        res = roleMiddleware.handler(requestMock)
        assert res == True

        try:
            roleMiddleware = RoleMiddleware(["foo"])
            res = roleMiddleware.handler(requestMock)
            assert False
        except:
            assert True
