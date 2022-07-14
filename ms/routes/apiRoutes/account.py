from ms.controllers import AccountController
from ms.middlewares import AuthMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/profile')
@middleware(AuthMiddleware)
def profile():
    return AccountController.action("profile")


@api.route('/profile', methods=['PUT'])
@middleware(AuthMiddleware)
def update():
    return AccountController.action('updateProfile')


@api.route('/profile/account', methods=['PUT'])
@middleware(AuthMiddleware)
def update_account():
    return AccountController.action('updateAccount')


@api.route('/profile/auth', methods=['PUT'])
@middleware(AuthMiddleware)
def update_auth():
    return AccountController.action('updateAuth')


@api.route('/profile/update-password', methods=['POST'])
@middleware(AuthMiddleware)
def updatePassword():
    return AccountController.action("updatePassword")


@api.route('/profile/permissions')
@middleware(AuthMiddleware)
def permissions():
    return AccountController.action("permissions")
