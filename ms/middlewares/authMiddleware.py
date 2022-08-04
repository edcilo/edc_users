from flask import abort
from ms.helpers.jwt import JwtHelper
from ms.repositories import UserRepository
from .middleware import Middleware


class AuthMiddleware(Middleware):
    def handler(self, request):
        jwtHelper = JwtHelper()
        userRepo = UserRepository()
        auth = request.headers.get('Authorization')

        if not auth:
            abort(401)

        valid = jwtHelper.check(auth)

        if not valid:
            abort(401)

        payload = jwtHelper.decode(auth)
        user = userRepo.find(payload['id'], fail=False)
        if not user:
            abort(401)

        payload['user'] = user
        setattr(request, 'auth', payload)

        return True
