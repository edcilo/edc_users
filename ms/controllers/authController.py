from flask import jsonify, request
from flaskFormRequest.decorators import form_validator
from ms import app
from ms.forms import AuthLoginForm, AuthRegisterForm
from ms.helpers.jwt import JwtHelper
from ms.repositories import UserRepository
from ms.serializers import JwtSerializer
from .controller import Controller


class AuthController(Controller):
    def __init__(self):
        self.jwt = JwtHelper()
        self.userRepo = UserRepository()

    def get_token(self, user):
        serializer = JwtSerializer(user)
        return self.jwt.get_tokens(serializer.get_data())

    @form_validator(AuthRegisterForm)
    def register(self, form):
        user = self.userRepo.add(form.data)
        token = self.get_token(user)
        return jsonify(token), 201

    @form_validator(AuthLoginForm)
    def login(self, form):
        username = form.data.get('username')
        password = form.data.get('password')
        user = self.userRepo.find_optional(
            {'phone': username, 'email': username}, fail=False)
        if user is None or not user.verify_password(password):
            return jsonify({
                'message': 'The credentials do not match our records.'
            }), 400
        token = self.get_token(user)
        return jsonify(token), 200

    def refresh_token(self):
        user = request.auth.get('user')
        token = self.get_token(user)
        return jsonify(token), 200

    def check(self):
        return jsonify(), 204
