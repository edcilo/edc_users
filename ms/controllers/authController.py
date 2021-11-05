from flask import jsonify, Response
from ms.forms import RegisterForm, LoginForm
from ms.helpers.jwt import jwtHelper
from ms.repositories import userRepo
from ms.serializers import UserSerializer, JwtSerializer
from ms.helpers.decorators import form_validator


class AuthController():
    @form_validator(RegisterForm)
    def register(self, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'username', 'password'))
        user = userRepo.add(data)
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    @form_validator(LoginForm)
    def login(self, form) -> tuple[Response, int]:
        user = userRepo.find_by_attr('username', form.username.data)
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    def refresh(self, payload: dict) -> tuple[Response, int]:
        user = userRepo.find(payload.get('id'), fail=True)
        serializer = JwtSerializer(user)
        token = jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    def profile(self, payload: dict) -> tuple[Response, int]:
        user = userRepo.find(payload.get('id'), fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200


authController = AuthController()
