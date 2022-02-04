from flask import abort
from .middleware import MiddlewareBase


class RoleMiddleware(MiddlewareBase):
    def __init__(self, *args) -> None:
        self.roles = args

    def handler(self, request) -> None:
        if hasattr(request, 'auth'):
            auth = request.auth
            role = auth.get('role', None)

            if role is not None and 'name' in role and role.get('name') in self.roles:
                return True

        abort(403)
