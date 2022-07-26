from ms.controllers import AppController
from ms.middlewares import AuthMiddleware, PermissionMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/admin/apps')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - list',))
def api_app_list():
    return AppController.action('list')


@api.route('/admin/apps', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - create',))
def api_app_create():
    return AppController.action('create')


@api.route('/admin/apps/<id>')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - detail',))
def api_app_detail(id):
    return AppController.action('detail', id)


@api.route('/admin/apps/<id>/token', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - generate token',))
def api_app_generate_token(id):
    return AppController.action('generate_token', id)


@api.route('/admin/apps/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - update',))
def api_app_update(id):
    return AppController.action('update', id)


@api.route('/admin/apps/<id>/permissions')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - detail',))
def api_app_permissions(id):
    return AppController.action('permissions', id)


@api.route('/admin/apps/<id>/sync-permissions', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - permissions',))
def api_app_sync_permissions(id):
    return AppController.action('sync_permissions', id)


@api.route('/admin/apps/<id>/sync-roles', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - roles',))
def api_app_sync_roles(id):
    return AppController.action('sync_roles', id)


@api.route('/admin/apps/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - delete',))
def api_app_delete(id):
    return AppController.action('delete', id)
