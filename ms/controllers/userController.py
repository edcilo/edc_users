from flask import jsonify
from ms.forms import RegisterForm, LoginForm
from ms.helpers.jwt import jwtHelper
from ms.repositories import userRepo
from ms.serializers import UserSerializer


class UserController():
    def register(self):
        form = RegisterForm()

        if not form.validate_on_submit():
            return jsonify({ "errors": form.errors }), 400

        data = userRepo.form_to_dict(form)
        user = userRepo.add(data)
        serializer = UserSerializer(user)

        return jsonify(serializer.data), 200

    def login(self):
        form = LoginForm()

        if not form.validate_on_submit():
            return jsonify({ "errors": form.errors }), 400

        user = userRepo.find_by_attr('username', form.username.data)
        serializer = UserSerializer(user)

        token = jwtHelper.get_tokens(serializer.data)

        return jsonify(token), 200

    def refresh(self):
        return 'refresh from controller'

    def profile(self):
        return 'profile from controller'


userController = UserController()
