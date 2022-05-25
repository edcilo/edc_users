from ms.controllers import PermissionController
from ms.middlewares import AuthMiddleware, RoleMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/admin/permissions')
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def permission_paginate():
    return PermissionController.action('paginate')


@api.route('/admin/permissions/list')
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def permission_list():
    return PermissionController.action('list')


@api.route('/admin/permission', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def permission_create():
    return PermissionController.action('create')


@api.route('/admin/permission/<id>')
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def permission_detail(id):
    return PermissionController.action('detail', id)


@api.route('/admin/permission/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def permission_update(id):
    return PermissionController.action('update', id)


@api.route('/admin/permission/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def permission_delete(id):
    return PermissionController.action('delete', id)
