from typing import Type
from flask import jsonify, Response

from ms.decorators import form_validator
from ms.forms import CreateForm, PaginateForm, UpdateForm, UpdatePasswordForm
from ms.forms.form import FormRequest
from ms.repositories import userRepo
from ms.serializers import UserSerializer


class AdminController():
    @form_validator(PaginateForm, method='GET')
    def list(self, form: Type[FormRequest]) -> tuple[Response, int]:
        params = {
            'paginate': True,
            'search': form.data['q'],
            'order': form.data['order'] or 'desc',
            'order_column': form.data['order_column'] or 'id',
            'page': form.data['page'] or 1,
            'per_page': form.data['per_page'] or 15,
        }
        collection = userRepo.all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateForm)
    def create(self, form: Type[FormRequest]) -> tuple[Response, int]:
        user = userRepo.add(form.data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 201

    def detail(self, id: str) -> tuple[Response, int]:
        user = userRepo.find(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdateForm)
    def update(self, id: str, form: Type[FormRequest]) -> tuple[Response, int]:
        user = userRepo.update(id, form.data, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdatePasswordForm)
    def update_password(self, id, form: Type[FormRequest]) -> tuple[Response, int]:
        userRepo.update_password(id, form.data.get('password'), fail=True)
        return jsonify(), 204

    def activate(self, id: str) -> tuple[Response, int]:
        userRepo.activate(id, fail=True)
        return jsonify(), 204

    def deactivate(self, id: str) -> tuple[Response, int]:
        userRepo.deactivate(id, fail=True)
        return jsonify(), 204

    def soft_delete(self, id: str) -> tuple[Response, int]:
        userRepo.soft_delete(id, fail=True)
        return jsonify(), 204

    def restore(self, id: str) -> tuple[Response, int]:
        userRepo.restore(id, fail=True)
        return jsonify(), 204

    def delete(self, id: str) -> tuple[Response, int]:
        userRepo.delete(id, fail=True)
        return jsonify({}), 204
