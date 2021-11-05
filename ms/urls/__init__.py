from flask import jsonify
from ms import app
from ms.controllers import userController
from ms.middlewares import auth


@app.route("/")
def hello_world():
    return jsonify({
        "data": {
            "name": app.config.get('APP_NAME'),
            "version": app.config.get('APP_VERSION'),
        },
        "code": 200
    }), 200


@app.route('/register', methods=['POST'])
def register():
    return userController.register()


@app.route('/login', methods=['POST'])
def login():
    return userController.login()


@app.route('/refresh', methods=['POST'])
@auth.auth
def refresh():
    return userController.refresh()


@app.route('/check', methods=['POST'])
@auth.auth
def check():
    return jsonify({}), 200


@app.route('/profile')
@auth.auth
def profile():
    return userController.profile()


@app.route('/<id>')
def detail(id):
    return userController.detail(id)


@app.route('/<id>', methods=['PUT'])
def update(id):
    return userController.update(id)
