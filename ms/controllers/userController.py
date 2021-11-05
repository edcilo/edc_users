from flask import jsonify, Response
from ms.forms import RegisterForm, LoginForm, UpdateForm
from ms.helpers.jwt import jwtHelper
from ms.repositories import userRepo
from ms.serializers import UserSerializer
from ms.helpers.decorators import form_validator


class UserController():
    @form_validator(RegisterForm)
    def register(self, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'username', 'password'))
        user = userRepo.add(data)
        serializer = UserSerializer(user)
        return jsonify(serializer.data), 200

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

    def detail(self, id: int) -> tuple[Response, int]:
        user = userRepo.find(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.data), 200

    @form_validator(UpdateForm)
    def update(self, id, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'username'))
        user = userRepo.update(id, data, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.data), 200


userController = UserController()
