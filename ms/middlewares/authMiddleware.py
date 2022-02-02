from flask import abort
from ms.helpers.jwt import jwtHelper
from ms.repositories import UserRepository, userRepository
from .middleware import MiddlewareBase


class AuthMiddleware(MiddlewareBase):
    def handler(self, request) -> None:
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
