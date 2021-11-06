from flask import jsonify, Response, request
from ms.forms import CreateForm, UpdateForm, PaginateForm
from ms.repositories import userRepo
from ms.serializers import UserSerializer
from ms.helpers.decorators import form_validator


class UserController():
    @form_validator(PaginateForm, 'GET')
    def list(self, form):
        params = {
            'paginate': True,
            'search': form.q.data,
            'order': form.order.data or 'desc',
            'page': form.page.data or 1,
            'per_page': form.per_page.data or 15,
        }
        collection = userRepo.get_all(**params)
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateForm)
    def create(self, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'phone', 'password'))
        user = userRepo.add(data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def detail(self, id: int) -> tuple[Response, int]:
        user = userRepo.find(id, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdateForm)
    def update(self, id, form) -> tuple[Response, int]:
        data = userRepo.form_to_dict(form, ('email', 'username'))
        user = userRepo.update(id, data, fail=True)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def delete(self, id: int) -> tuple[Response, int]:
        userRepo.delete(id, fail=True)
        return jsonify(), 204


userController = UserController()
