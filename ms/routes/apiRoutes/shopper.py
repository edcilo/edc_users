from ms.controllers import ShopperController
from ms.middlewares import AuthMiddleware, PermissionMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/shopper', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Shopper - create',))
def api_client_create():
    return ShopperController.action('create')


@api.route('/shopper/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Shopper - update',))
def api_client_update(id):
    return ShopperController.action('update', id)


@api.route("/shopper/<id>/files", methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Shopper - upload files',))
def api_client_upload_id_files(id):
    return ShopperController.action('upload_id_files', id)
