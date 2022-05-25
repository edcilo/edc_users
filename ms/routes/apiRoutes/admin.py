from ms.controllers import AdminUserController
from ms.middlewares import AuthMiddleware, PermissionMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/admin')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - list',))
def api_users_list():
    return AdminUserController.action('list')


@api.route('/admin/trash')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - list',))
def api_users_trash():
    return AdminUserController.action('trash')


@api.route('/admin', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - create',))
def api_users_create():
    return AdminUserController.action('create')


@api.route('/admin/<id>')
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - detail',))
def api_users_detail(id):
    return AdminUserController.action('detail', id)


@api.route('/admin/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - update',))
def api_users_update(id):
    return AdminUserController.action('update', id)


@api.route('/admin/<id>/password', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - update password',))
def api_users_update_password(id):
    return AdminUserController.action('update_password', id)


@api.route('/admin/<id>/permissions', methods=['GET'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - detail',))
def api_users_permissions(id):
    return AdminUserController.action('permissions', id)


@api.route('/admin/<id>/sync-permissions', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - permissions',))
def api_users_sync_permissions(id):
    return AdminUserController.action('sync_permissions', id)


@api.route('/admin/<id>/sync-roles', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - roles',))
def api_users_sync_roles(id):
    return AdminUserController.action('sync_roles', id)


@api.route('/admin/<id>/activate', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - activate',))
def api_users_activate(id):
    return AdminUserController.action('activate', id)


@api.route('/admin/<id>/activate', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - activate',))
def api_users_deactivate(id):
    return AdminUserController.action('deactivate', id)


@api.route('/admin/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - soft delete',))
def api_users_soft_delete(id):
    return AdminUserController.action('soft_delete', id)


@api.route('/admin/<id>/restore', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - restore',))
def api_users_restore(id):
    return AdminUserController.action('restore', id)


@api.route('/admin/<id>/hard', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(PermissionMiddleware, permissions=('User - delete',))
def api_users_delete(id):
    return AdminUserController.action('delete', id)
