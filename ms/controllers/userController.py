from flask import jsonify
from ms.repositories import userRepo
from ms.forms import RegisterForm
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
        return 'login form controller'

    def refresh(self):
        return 'refresh from controller'

    def profile(self):
        return 'profile from controller'


userController = UserController()
