from flask import jsonify, request, Response
from ms.serializers import AccountSerializer


class AccountController():
    def profile(self) -> tuple[Response, int]:
        user = request.auth.get('user')
        serializer = AccountSerializer(user)
        return jsonify(serializer.get_data()), 200
