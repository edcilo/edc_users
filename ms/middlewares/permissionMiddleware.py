from flask import abort
from sqlalchemy import or_
from ms.models import Permission
from .middleware import Middleware


class PermissionMiddleware(Middleware):
    def __init__(self, permissions):
        self.permissions = permissions

    def handler(self, request):
        user = request.auth.get("user")

        if user.roles.filter_by(name="root").count() > 0:
            return True

        for permission in user.all_permissions:
            if permission.name in self.permissions:
                return True

        abort(403)
