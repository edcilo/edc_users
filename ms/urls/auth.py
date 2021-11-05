from flask import jsonify
from ms import app
from ms.controllers import authController
from ms.middlewares import auth


@app.route('/register', methods=['POST'])
def register():
    return authController.register()


@app.route('/login', methods=['POST'])
def login():
    return authController.login()


@app.route('/refresh', methods=['POST'])
@auth.auth
def refresh():
    return authController.refresh()


@app.route('/check', methods=['POST'])
@auth.auth
def check():
    return jsonify({}), 200


@app.route('/profile')
@auth.auth
def profile():
    return authController.profile()
