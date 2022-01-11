from ms import app
from ms.controllers import authController
from ms.middlewares import middleware, AuthMiddleware


url_prefix = app.config.get('URL_PREFIX')

@app.route(f'{url_prefix}/register', methods=['POST'])
def register():
    return authController.register()


@app.route(f'{url_prefix}/login', methods=['POST'])
def login():
    return authController.login()


@app.route(f'{url_prefix}/refresh', methods=['POST'])
@middleware(AuthMiddleware)
def refresh():
    return authController.refresh()


@app.route(f'{url_prefix}/check', methods=['POST'])
@middleware(AuthMiddleware)
def check():
    return {}, 204
