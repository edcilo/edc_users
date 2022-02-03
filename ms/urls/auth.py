from ms import app
from ms.controllers import AuthController
from ms.middlewares import middleware, AuthMiddleware


url_prefix = app.config.get('URL_PREFIX')


@app.route(f'{url_prefix}/register', methods=['POST'])
def register():
    return AuthController().register()


@app.route(f'{url_prefix}/login', methods=['POST'])
def login():
    return AuthController().login()


@app.route(f'{url_prefix}/refresh', methods=['POST'])
@middleware(AuthMiddleware())
def refresh():
    return AuthController().refresh()


@app.route(f'{url_prefix}/check', methods=['POST'])
@middleware(AuthMiddleware())
def check():
    return {}, 204
