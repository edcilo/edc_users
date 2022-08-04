from flask import jsonify
from flaskFormRequest.decorators import form_validator
from ms import app
from ms.forms import (
    AdminCreatePermissionForm,
    AdminListPermissionsForm,
    AdminUpdatePermissionForm
)
from ms.repositories import PermissionRepository
from ms.serializers import PermissionSerializer
from .controller import Controller


class PermissionController(Controller):
    def __init__(self):
        self.permissionRepo = PermissionRepository()

    def list(self):
        collection = self.permissionRepo.all(**{
            'paginate': False,
            'order': 'asc',
            'order_column': 'name',
        })
        serializer = PermissionSerializer(collection, collection=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminListPermissionsForm)
    def paginate(self, form):
        collection = self.permissionRepo.all(**{
            'paginate': True,
            'per_page': form.data.get('per_page', 15),
            'page': form.data.get('page', 1),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'created_at'),
            'search': form.data.get('q', None)
        })
        serializer = PermissionSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminCreatePermissionForm)
    def create(self, form):
        permission = self.permissionRepo.add(form.data)
        serializer = PermissionSerializer(permission)
        return jsonify(serializer.get_data()), 201

    def detail(self, id):
        permission = self.permissionRepo.find(id)
        serializer = PermissionSerializer(permission)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminUpdatePermissionForm)
    def update(self, id, form):
        permission = self.permissionRepo.update(id, form.data)
        serializer = PermissionSerializer(permission)
        return jsonify(serializer.get_data()), 200

    def delete(self, id):
        permission, success = self.permissionRepo.delete(id)
        if success:
            return jsonify(None), 204
        else:
            return jsonify({
                "message": "It's not possible delete a permission with the attribute 'fixed' like true",
                "code": 403
            }), 403
