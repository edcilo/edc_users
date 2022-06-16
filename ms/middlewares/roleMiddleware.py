from flask import abort
from sqlalchemy import or_
from ms.models import Role
from .middleware import Middleware


class RoleMiddleware(Middleware):
    def __init__(self, roles):
        self.roles = roles

    def handler(self, request):
        user = request.auth.get("user")

        if user.roles.filter_by(name="root").count() > 0:
            return True

        filters = [Role.name == role for role in self.roles]
        if user.roles.filter(or_(*filters)).count() > 0:
            return True

        abort(403)
