from flask import abort
from ms.helpers.jwt import JwtHelper
from ms.repositories import UserRepository, AppRepository
from .middleware import Middleware


class AuthMiddleware(Middleware):
    def handler(self, request):
        jwtHelper = JwtHelper()
        userRepo = UserRepository()
        appRepo = AppRepository()
        auth = request.headers.get('Authorization')

        if not auth:
            abort(401)

        valid = jwtHelper.check(auth)
        if not valid:
            abort(401)

        payload = jwtHelper.decode(auth)
        entity = userRepo.find(payload['id'], fail=False)

        if not entity:
            entity = appRepo.find(payload['id'], fail=False)
            if not entity:
                abort(401)

        payload['user'] = entity
        setattr(request, 'auth', payload)

        return True
