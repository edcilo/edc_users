from flask import jsonify, request, Response
from ms.forms import RegisterForm, LoginForm
from ms.helpers.jwt import jwtHelper
from ms.repositories import userRepo
from ms.serializers import UserSerializer, JwtSerializer
from ms.decorators import form_validator


class AuthController():
    @form_validator(RegisterForm)
    def register(self, form) -> tuple[Response, int]:
        user = userRepo.add(form.data)
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    @form_validator(LoginForm)
    def login(self, form) -> tuple[Response, int]:
        username = form.data.get('username')
        password = form.data.get('password')
        user = userRepo.find_optional(
            {'phone': username, 'email': username}, fail=True)
        print(user)
        if not user.verify_password(password):
            return jsonify({
                'message': 'The credentials do not match our records.'
            }), 400
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    def refresh(self) -> tuple[Response, int]:
        user = request.auth.get('user')
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    def check(self) -> tuple[Response, int]:
        return jsonify(), 204

    def profile(self) -> tuple[Response, int]:
        user = request.auth.get('user')
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200


authController = AuthController()
