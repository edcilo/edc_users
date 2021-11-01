from flask import jsonify
from ms import app
from ms.controllers import userController


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
def register(): return userController.register()

@app.route('/login', methods=['POST'])
def login(): return userController.login()

@app.route('/refresh', methods=['POST'])
def refresh(): return userController.refresh()

@app.route('/check', methods=['POST'])
def check(): return userController.check()

@app.route('/profile')
def profile(): return userController.profile()
