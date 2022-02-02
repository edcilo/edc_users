from ms import app
from ms.controllers import roleController
from ms.middlewares import middleware, AuthMiddleware


url_prefix = app.config.get('URL_PREFIX')

@app.route(f'{url_prefix}/admin/roles')
@middleware(AuthMiddleware)
def list_roles():
    return roleController.list()


@app.route(f'{url_prefix}/admin/roles', methods=['POST'])
@middleware(AuthMiddleware)
def create_role():
    return roleController.create()


@app.route(f'{url_prefix}/admin/role/<id>')
@middleware(AuthMiddleware)
def role_detail(id):
    return roleController.detail(id)


@app.route(f'{url_prefix}/admin/role/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
def update_role(id):
    return roleController.update(id)


@app.route(f'{url_prefix}/admin/role/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
def delete_role(id):
    return roleController.delete(id)
