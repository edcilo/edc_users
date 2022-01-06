from ms import app
from ms.controllers import authController
from ms.middlewares import middleware, AuthMiddleware


@app.route('/api/v1/users/register', methods=['POST'])
def register():
    return authController.register()


@app.route('/api/v1/users/login', methods=['POST'])
def login():
    return authController.login()


@app.route('/api/v1/users/refresh', methods=['POST'])
@middleware(AuthMiddleware)
def refresh():
    return authController.refresh()


@app.route('/api/v1/users/check', methods=['POST'])
@middleware(AuthMiddleware)
def check():
    return {}, 204
