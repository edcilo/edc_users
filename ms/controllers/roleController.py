from flask import jsonify, request
from flaskFormRequest.decorators import form_validator
from ms import app
from ms.forms import (
    AdminCreateRoleForm,
    AdminListRolesForm,
    AdminUpdateRoleForm,
)
from ms.repositories import RoleRepository
from ms.serializers import RoleSerializer, RolePermissionsSerializer
from .controller import Controller


class RoleController(Controller):
    def __init__(self):
        self.roleRepo = RoleRepository()

    def list(self):
        collection = self.roleRepo.all(**{
            'paginate': False,
            'order': 'asc',
            'order_column': 'name',
        })
        serializer = RoleSerializer(collection, collection=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminListRolesForm)
    def paginate(self, form):
        collection = self.roleRepo.all(**{
            'paginate': True,
            'per_page': form.data.get('per_page', 15),
            'page': form.data.get('page', 1),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'created_at'),
            'search': form.data.get('q', None)
        })
        serializer = RoleSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminCreateRoleForm)
    def create(self, form):
        role = self.roleRepo.add(form.data)
        serializer = RoleSerializer(role)
        return jsonify(serializer.get_data()), 201

    def detail(self, id):
        role = self.roleRepo.find(id)
        serializer = RolePermissionsSerializer(role)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminUpdateRoleForm)
    def update(self, id, form):
        role, success = self.roleRepo.update(id, form.data)
        if not success:
            return jsonify({
                "message": "It's not possible modify the root role",
                "code": 403
            }), 403
        serializer = RoleSerializer(role)
        return jsonify(serializer.get_data()), 200

    def sync_permissions(self, id):
        data = request.get_json()
        self.roleRepo.sync_permissions(id, data.get("permissions"))
        return jsonify(None), 204

    def delete(self, id):
        role, success = self.roleRepo.delete(id)
        if success:
            return jsonify(None), 204
        else:
            return jsonify({
                "message": "It's not possible delete a role with the attribute 'fixed' like true",
                "code": 403
            }), 403
