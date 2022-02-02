from typing import Type
from flask import jsonify, Response
from flaskFormRequest import FormRequest

from ms.decorators import form_validator
from ms.forms import CreateRoleForm, RolePaginateForm, UpdateRoleForm
from ms.repositories import RoleRepository
from ms.serializers import RoleSerializer


class RoleController():
    def __init__(self) -> None:
        self.repo = RoleRepository()

    @form_validator(RolePaginateForm)
    def list(self, form: Type[FormRequest]) -> tuple[Response, int]:
        params = {
            'paginate': True,
            'search': form.data.get('q'),
            'order': form.data.get('order', 'desc'),
            'order_column': 'name',
            'page': form.data.get('page', 1),
            'per_page': form.data.get('per_page', 15),
        }
        collection = self.repo.all(**params)
        serializer = RoleSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(CreateRoleForm)
    def create(self, form: Type[FormRequest]) -> tuple[Response, int]:
        role = self.repo.add(form.data)
        serializer = RoleSerializer(role)
        return jsonify(serializer.get_data()), 200

    def detail(self, id: str) -> tuple[Response, int]:
        role = self.repo.find(id, fail=True)
        serializer = RoleSerializer(role)
        return jsonify(serializer.get_data()), 200

    @form_validator(UpdateRoleForm)
    def update(self, id: str, form: Type[FormRequest]) -> tuple[Response, int]:
        role = self.repo.update(id, form.data, fail=True)
        serializer = RoleSerializer(role)
        return jsonify(serializer.get_data()), 200

    def delete(self, id: str) -> tuple[Response, int]:
        role = self.repo.delete(id, fail=True)
        if role is None:
            return jsonify({'errors':
                {"uuid": "Cannot delete a role with related users"}}), 400
        return jsonify({}), 204
