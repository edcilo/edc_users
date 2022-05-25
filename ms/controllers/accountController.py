from flask import jsonify, request
from ms.serializers import UserSerializer, PermissionSerializer, serializer
from .controller import Controller


class AccountController(Controller):
    def profile(self):
        user = request.auth.get('user')
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    def permissions(self):
        user = request.auth.get('user')
        permissions_serializer = PermissionSerializer(
            user.permissions.all(), collection=True)
        role_psermissions_serializer = PermissionSerializer(
            user.all_permissions, collection=True)
        return jsonify({
            "permissions": permissions_serializer.get_data(),
            "roles_permissions": role_psermissions_serializer.get_data()
        }), 200
