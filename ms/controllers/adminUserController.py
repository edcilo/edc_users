from flask import jsonify, request
from flaskFormRequest.decorators import form_validator
from ms.forms import (
    AdminListUsersForm,
    AdminCreateUserForm,
    AdminUpdateUserForm,
    AdminUpdateUserPasswordForm)
from ms.repositories import UserRepository, RoleRepository
from ms.serializers import UserSerializer, UserProfileSerializer, PermissionSerializer
from .controller import Controller


class AdminUserController(Controller):
    def __init__(self):
        self.userRepo = UserRepository()
        self.roleRepo = RoleRepository()

    @form_validator(AdminListUsersForm)
    def list(self, form):
        collection = self.userRepo.all(**{
            'paginate': True,
            'per_page': form.data.get('per_page', 15),
            'page': form.data.get('page', 1),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'created_at'),
            'search': form.data.get('q', None)
        })
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminListUsersForm)
    def trash(self, form):
        collection = self.userRepo.all(**{
            'deleted': True,
            'paginate': True,
            'per_page': form.data.get('per_page', 15),
            'page': form.data.get('page', 1),
            'order': form.data.get('order', 'desc'),
            'order_column': form.data.get('order_column', 'created_at'),
            'search': form.data.get('q', None)
        })
        serializer = UserSerializer(collection, paginate=True)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminCreateUserForm)
    def create(self, form):
        user = self.userRepo.add(form.data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 201

    def detail(self, id):
        user = self.userRepo.find(id)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminUpdateUserForm)
    def update(self, id, form):
        user = self.userRepo.update(id, form.data)
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AdminUpdateUserPasswordForm)
    def update_password(self, id, form):
        self.userRepo.update_password(id, form.data.get('password'))
        return jsonify(), 204

    def permissions(self, id):
        user = self.userRepo.find(id)
        permissions_serializer = PermissionSerializer(
            user.permissions.all(), collection=True)
        role_psermissions_serializer = PermissionSerializer(
            user.all_permissions, collection=True)
        return jsonify({
            "permissions": permissions_serializer.get_data(),
            "roles_permissions": role_psermissions_serializer.get_data()
        }), 200

    # TODO: add form validator
    def sync_permissions(self, id):
        data = request.get_json()
        self.userRepo.sync_permissions(id, data.get("permissions", []))
        return jsonify(None), 204

    # TODO: add form validator
    def sync_roles(self, id):
        data = request.get_json()
        self.userRepo.sync_roles(id, data.get("roles", []))
        return jsonify(None), 204

    def activate(self, id):
        self.userRepo.activate(id)
        return jsonify(), 204

    def deactivate(self, id):
        self.userRepo.deactivate(id)
        return jsonify(), 204

    def soft_delete(self, id):
        self.userRepo.soft_delete(id)
        return jsonify(), 204

    def restore(self, id):
        self.userRepo.restore(id)
        return jsonify(), 204

    def delete(self, id):
        self.userRepo.delete(id)
        return jsonify(None), 204
