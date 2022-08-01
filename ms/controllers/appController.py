from flask import jsonify, request
from flaskFormRequest.decorators import form_validator
from ms.forms import (
    AppListForm,
    AppCreateForm,
    AppUpdateForm)
from ms.helpers.jwt import JwtHelper
from ms.repositories import AppRepository
from ms.serializers import (
    AppSerializer,
    JwtSerializer,
    PermissionSerializer)
from .controller import Controller


class AppController(Controller):
    def __init__(self):
        self.jwt = JwtHelper(token_lifetime=1576800000)
        self.appRepo = AppRepository()

    @form_validator(AppListForm)
    def list(self, form):
        collection = self.appRepo.all(**{
            'paginate': True,
            'per_page': form.data.get('per_page', 15),
            'page': form.data.get('page', 1),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'created_at'),
            'search': form.data.get('q', None)
        })
        serializer = AppSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AppCreateForm)
    def create(self, form):
        app = self.appRepo.add(form.data)
        serializer = AppSerializer(app)
        return jsonify(serializer.get_data()), 201

    def detail(self, id):
        app = self.appRepo.find(id)
        serializer = AppSerializer(app)
        return jsonify(serializer.get_data()), 200

    def generate_token(self, id):
        app = self.appRepo.find(id)
        serializer = JwtSerializer(app)
        token = self.jwt.get_tokens(serializer.get_data())
        return jsonify(token), 200

    @form_validator(AppUpdateForm)
    def update(self, id, form):
        app = self.appRepo.update(id, form.data)
        serializer = AppSerializer(app)
        return jsonify(serializer.get_data()), 200

    def permissions(self, id):
        app = self.appRepo.find(id)
        permissions_serializer = PermissionSerializer(
            app.permissions.all(), collection=True)
        role_permissions_serializer = PermissionSerializer(
            app.all_permissions, collection=True)
        return jsonify({
            "permissions": permissions_serializer.get_data(),
            "roles_permissions": role_permissions_serializer.get_data()
        }), 200

    def sync_permissions(self, id):
        data = request.get_json()
        self.appRepo.sync_permissions(id, data.get('permissions', []))
        return jsonify(None), 204

    def sync_roles(self, id):
        data = request.get_json()
        self.appRepo.sync_roles(id, data.get('roles', []))
        return jsonify(None), 204

    def delete(self, id):
        self.appRepo.delete(id)
        return jsonify(None), 204
