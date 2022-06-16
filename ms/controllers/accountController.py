from flask import jsonify, request
from flaskFormRequest.decorators import form_validator
from ms.forms import AccountUpdatePassword
from ms.repositories import UserRepository
from ms.serializers import UserSerializer, PermissionSerializer
from .controller import Controller


class AccountController(Controller):
    def __init__(self):
        self.userRepo = UserRepository()

    def profile(self):
        user = request.auth.get('user')
        serializer = UserSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AccountUpdatePassword)
    def updatePassword(self, form):
        user = request.auth.get('user')
        self.userRepo.update_password(user.id, form.data.get('password'))
        return jsonify(), 204

    def permissions(self):
        user = request.auth.get('user')
        permissions_serializer = PermissionSerializer(
            user.all_permissions, collection=True)
        return jsonify(permissions_serializer.get_data()), 200
