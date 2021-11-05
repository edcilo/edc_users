from flask import jsonify, Response
from ms.forms import RegisterForm, LoginForm
from ms.helpers.jwt import jwtHelper
from ms.repositories import userRepo
from ms.serializers import UserSerializer
from ms.helpers.decorators import form_validator


class AuthController():
    @form_validator(RegisterForm)
    def register(self, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'username', 'password'))
        user = userRepo.add(data)
        serializer = UserSerializer(user)
        token = jwtHelper.get_tokens(serializer.data)
        return jsonify(token), 200

    @form_validator(LoginForm)
    def login(self, form) -> tuple[Response, int]:
        user = userRepo.find_by_attr('username', form.username.data)
        serializer = UserSerializer(user)
        token = jwtHelper.get_tokens(serializer.data)
        return jsonify(token), 200

    def refresh(self) -> tuple[Response, int]:
        return 'refresh from controller', 200

    def profile(self) -> tuple[Response, int]:
        return 'profile from controller', 200


authController = AuthController()
