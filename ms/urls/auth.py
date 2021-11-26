from ms import app
from ms.controllers import authController
from ms.middlewares import middleware, AuthMiddleware


@app.route('/register', methods=['POST'])
def register():
    return authController.register()


@app.route('/login', methods=['POST'])
def login():
    return authController.login()


@app.route('/refresh', methods=['POST'])
@middleware(AuthMiddleware)
def refresh():
    return authController.refresh()


@app.route('/check', methods=['POST'])
@middleware(AuthMiddleware)
def check():
    return {}, 204
