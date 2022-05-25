from ms.controllers import RoleController
from ms.middlewares import AuthMiddleware, RoleMiddleware
from ms.middlewares.middleware import middleware
from ms.routes.blueprints import api


@api.route('/admin/roles')
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_paginate():
    return RoleController.action('paginate')


@api.route('/admin/roles/list')
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_list():
    return RoleController.action('list')


@api.route('/admin/role', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_create():
    return RoleController.action('create')


@api.route('/admin/role/<id>')
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_detail(id):
    return RoleController.action('detail', id)


@api.route('/admin/role/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_update(id):
    return RoleController.action('update', id)


@api.route('/admin/role/<id>/sync-permissions', methods=['POST'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_sync_permissions(id):
    return RoleController.action('sync_permissions', id)


@api.route('/admin/role/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
@middleware(RoleMiddleware, roles=('root',))
def role_delete(id):
    return RoleController.action('delete', id)
