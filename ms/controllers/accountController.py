from flask import jsonify, request
from flaskFormRequest.decorators import form_validator
from ms.forms import (
    AccountUpdateForm,
    AccountUpdateAuthForm,
    AccountUpdatePasswordForm,
    AccountUpdateProfileForm)
from ms.repositories import ClientRepository, UserRepository
from ms.serializers import UserProfileSerializer, PermissionSerializer
from .controller import Controller


class AccountController(Controller):
    def __init__(self):
        self.clientRepo = ClientRepository()
        self.userRepo = UserRepository()

    def profile(self):
        user = request.auth.get('user')
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AccountUpdateForm)
    def updateAccount(self, form):
        user = request.auth.get('user')
        data = {
            "name": form.data.get("name"),
            "lastname": form.data.get("lastname"),
            "mothername": form.data.get("mothername"),
        }
        user = self.userRepo.update(user.id, data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AccountUpdateAuthForm)
    def updateAuth(self, form):
        user = request.auth.get('user')
        data = {
            "email": form.data.get("email"),
            "phone": form.data.get("phone"),
        }
        user = self.userRepo.update(user.id, data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AccountUpdateProfileForm)
    def updateProfile(self, form):
        user = request.auth.get('user')
        user = self.clientRepo.update(user, form.data)
        serializer = UserProfileSerializer(user)
        return jsonify(serializer.get_data()), 200

    @form_validator(AccountUpdatePasswordForm)
    def updatePassword(self, form):
        user = request.auth.get('user')
        self.userRepo.update_password(user.id, form.data.get('password'))
        return jsonify(), 204

    def permissions(self):
        user = request.auth.get('user')
        permissions_serializer = PermissionSerializer(
            user.all_permissions, collection=True)
        return jsonify(permissions_serializer.get_data()), 200
