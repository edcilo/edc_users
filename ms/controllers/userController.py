import uuid
from flask import jsonify, request, Response
from ms.decorators import form_validator
from ms.forms import BaseForm, CreateForm, UpdateForm, PaginateForm
from ms.repositories import userRepo
from ms.serializers import UserSerializer


class UserController():
    @form_validator(PaginateForm, method='GET')
    def list(self, form) -> tuple[Response, int]:
        params = {
            'paginate': True,
            'search': form.data['q'],
            'order': form.data['order'] or 'desc',
            'page': form.data['page'] or 1,
            'per_page': form.data['per_page'] or 15,
        }
        collection = userRepo.all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateForm)
    def create(self, form) -> tuple[Response, int]:
        user = userRepo.add(form.data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def detail(self, id: uuid) -> tuple[Response, int]:
        user = userRepo.find(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdateForm)
    def update(self, id: uuid, form) -> tuple[Response, int]:
        user = userRepo.update(id, form.data, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def activate(self, id: uuid) -> tuple[Response, int]:
        userRepo.activate(id, fail=True)
        return jsonify(), 204

    def deactivate(self, id: uuid) -> tuple[Response, int]:
        userRepo.deactivate(id, fail=True)
        return jsonify(), 204

    def soft_delete(self, id: uuid) -> tuple[Response, int]:
        userRepo.soft_delete(id, fail=True)
        return jsonify(), 204

    def restore(self, id: uuid) -> tuple[Response, int]:
        user = userRepo.restore(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def delete(self, id: uuid) -> tuple[Response, int]:
        userRepo.delete(id, fail=True)
        return jsonify(), 204


userController = UserController()
