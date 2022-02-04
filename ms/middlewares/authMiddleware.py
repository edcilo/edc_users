from flask import abort
from ms.helpers.jwt import JwtHelper
from ms.repositories import UserRepository
from .middleware import MiddlewareBase


class AuthMiddleware(MiddlewareBase):
    def handler(self, request) -> None:
        jwtHelper = JwtHelper()
        userRepo = UserRepository()
        auth = request.headers.get('Authorization')

        if not auth:
            abort(403)

        valid = jwtHelper.check(auth)

        if not valid:
            abort(403)

        payload = jwtHelper.decode(auth)
        payload['user'] = userRepo.find(payload['id'], fail=True)

        setattr(request, 'auth', payload)
