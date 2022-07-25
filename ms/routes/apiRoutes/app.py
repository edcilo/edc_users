from ms.controllers import AppController
from ms.middlewares import AuthMiddleware, PermissionMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/admin/app')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - list',))
def api_app_list():
    return AppController.action('list')


@api.route('/admin/app', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - create',))
def api_app_create():
    return AppController.action('create')


@api.route('/admin/app/<id>')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - detail',))
def api_app_detail(id):
    return AppController.action('detail', id)


@api.route('/admin/app/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - update',))
def api_app_update(id):
    return AppController.action('update', id)


@api.route('/admin/app/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('App - delete',))
def api_app_delete(id):
    return AppController.action('delete', id)
