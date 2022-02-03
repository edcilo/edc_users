from flask import abort
from .middleware import MiddlewareBase


class RoleMiddleware(MiddlewareBase):
    def __init__(self, *args) -> None:
        self.roles = args

    def handler(self, request) -> None:
        if not hasattr(request, 'auth'):
            abort(403)

        auth = request.auth

        if 'role' not in auth:
            abort(403)

        role = auth.get('role')
        if 'name' not in role or not role.get('name') in self.roles:
            abort(403)
