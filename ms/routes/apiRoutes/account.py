from ms.controllers import AccountController
from ms.middlewares import AuthMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/profile')
@middleware(AuthMiddleware)
def profile():
    return AccountController.action("profile")

@api.route('/profile/update-password', methods=['POST'])
@middleware(AuthMiddleware)
def updatePassword():
    return AccountController.action("updatePassword")

@api.route('/profile/permissions')
@middleware(AuthMiddleware)
def permissions():
    return AccountController.action("permissions")
