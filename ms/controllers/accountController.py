from flask import jsonify, request
from ms.serializers import UserSerializer
from .controller import Controller


class AccountController(Controller):
    def profile(self):
        user = request.auth.get('user')
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200
