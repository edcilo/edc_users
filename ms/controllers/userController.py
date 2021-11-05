from flask import jsonify, Response
from ms.forms import RegisterForm, LoginForm, UpdateForm, CreateForm
from ms.helpers.jwt import jwtHelper
from ms.repositories import userRepo
from ms.serializers import UserSerializer
from ms.helpers.decorators import form_validator


class UserController():
    @form_validator(CreateForm)
    def create(self, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'username', 'password'))
        user = userRepo.add(data)
        serializer = UserSerializer(user)
        return jsonify(serializer.data), 200

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

    def delete(self, id: int) -> tuple[Response, int]:
        userRepo.delete(id, fail=True)
        return jsonify(), 204


userController = UserController()
