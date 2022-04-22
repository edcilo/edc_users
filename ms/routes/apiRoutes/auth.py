from ms.controllers import AuthController
from ms.middlewares import AuthMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/register', methods=['POST'])
def register():
    return AuthController.action('register')


@api.route('/login', methods=['POST'])
def login():
    return AuthController.action('login')


@api.route('/refresh', methods=['POST'])
@middleware(AuthMiddleware)
def refresh_token():
    return AuthController.action('refresh_token')


@api.route('/check', methods=['POST'])
@middleware(AuthMiddleware)
def check():
    return AuthController.action('check')
