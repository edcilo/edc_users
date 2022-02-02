from typing import Type
from flask import jsonify, Response
from flaskFormRequest import FormRequest

from ms.decorators import form_validator
from ms.forms import CreateForm, PaginateForm, UpdateForm, UpdatePasswordForm
from ms.repositories import UserRepository
from ms.serializers import UserSerializer


class AdminController():
    def __init__(self) -> None:
        self.userRepo = UserRepository()

    @form_validator(PaginateForm)
    def list(self, form: Type[FormRequest]) -> tuple[Response, int]:
        params = {
            'paginate': True,
            'search': form.data.get('q'),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'id'),
            'page': form.data.get('page', 1),
            'per_page': form.data.get('per_page', 15),
        }
        collection = self.userRepo.all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateForm)
    def create(self, form: Type[FormRequest]) -> tuple[Response, int]:
        user = self.userRepo.add(form.data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def detail(self, id: str) -> tuple[Response, int]:
        user = self.userRepo.find(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdateForm)
    def update(self, id: str, form: Type[FormRequest]) -> tuple[Response, int]:
        user = self.userRepo.update(id, form.data, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdatePasswordForm)
    def update_password(self, id, form: Type[FormRequest]) -> tuple[Response, int]:
        self.userRepo.update_password(id, form.data.get('password'), fail=True)
        return jsonify(), 204

    def activate(self, id: str) -> tuple[Response, int]:
        self.userRepo.activate(id, fail=True)
        return jsonify(), 204

    def deactivate(self, id: str) -> tuple[Response, int]:
        self.userRepo.deactivate(id, fail=True)
        return jsonify(), 204

    def soft_delete(self, id: str) -> tuple[Response, int]:
        self.userRepo.soft_delete(id, fail=True)
        return jsonify(), 204

    def restore(self, id: str) -> tuple[Response, int]:
        self.userRepo.restore(id, fail=True)
        return jsonify(), 204

    def delete(self, id: str) -> tuple[Response, int]:
        self.userRepo.delete(id, fail=True)
        return jsonify({}), 204
