from ms.controllers import ClientController
from ms.middlewares import AuthMiddleware, PermissionMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/client', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Client - create',))
def api_client_create():
    return ClientController.action('create')


@api.route('/client/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Client - update',))
def api_client_update(id):
    return ClientController.action('update', id)


@api.route("/client/<id>/files", methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('Client - upload files',))
def api_client_upload_id_files(id):
    return ClientController.action('upload_id_files', id)
