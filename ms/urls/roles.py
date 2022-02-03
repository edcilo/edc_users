from ms import app
from ms.controllers import RoleController
from ms.middlewares import middleware, AuthMiddleware, RoleMiddleware


url_prefix = app.config.get('URL_PREFIX')


@app.route(f'{url_prefix}/admin/roles')
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def list_roles():
    return RoleController().list()


@app.route(f'{url_prefix}/admin/roles', methods=['POST'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def create_role():
    return RoleController().create()


@app.route(f'{url_prefix}/admin/role/<id>')
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def role_detail(id):
    return RoleController().detail(id)


@app.route(f'{url_prefix}/admin/role/<id>', methods=['PUT'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def update_role(id):
    return RoleController().update(id)


@app.route(f'{url_prefix}/admin/role/<id>', methods=['DELETE'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def delete_role(id):
    return RoleController().delete(id)
