from flask import jsonify, request, Response
from ms.forms import RegisterForm, LoginForm
from ms.helpers.jwt import JwtHelper
from ms.repositories import RoleRepository, UserRepository
from ms.serializers import UserSerializer, JwtSerializer
from ms.decorators import form_validator


class AuthController():
    def __init__(self) -> None:
        self.repo = UserRepository()
        self.roleRepo = RoleRepository()
        self.jwtHelper = JwtHelper()

    @form_validator(RegisterForm)
    def register(self, form) -> tuple[Response, int]:
        form.data['role_id'] = self.roleRepo.find_by_attr("name", "client").id
        user = self.repo.add(form.data)
        serializer = JwtSerializer(user)
        token = self.jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    @form_validator(LoginForm)
    def login(self, form) -> tuple[Response, int]:
        username = form.data.get('username')
        password = form.data.get('password')
        user = self.repo.find_optional(
            {'phone': username, 'email': username}, fail=True)
        if not user.verify_password(password):
            return jsonify({
                'message': 'The credentials do not match our records.'
            }), 400
        serializer = JwtSerializer(user)
        token = self.jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    def refresh(self) -> tuple[Response, int]:
        user = request.auth.get('user')
        serializer = JwtSerializer(user)
        token = self.jwtHelper.get_tokens(serializer.get_data())
        return jsonify(token), 200

    def check(self) -> tuple[Response, int]:
        return jsonify(), 204
