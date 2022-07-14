from ms.controllers import ClientController
from ms.middlewares import AuthMiddleware, PermissionMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/client', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Client - create',))
def api_client_create():
    return ClientController.action('create')
