from ms import app
from ms.controllers import adminController
from ms.middlewares import middleware, AuthMiddleware, RoleMiddleware


url_prefix = app.config.get('URL_PREFIX')

@app.route(f'{url_prefix}/admin')
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin', 'client'))
def list():
    return adminController.list()


@app.route(f'{url_prefix}/admin', methods=['POST'])
@middleware(AuthMiddleware())
def create():
    return adminController.create()


@app.route(f'{url_prefix}/admin/<id>')
@middleware(AuthMiddleware())
def detail(id):
    return adminController.detail(id)


@app.route(f'{url_prefix}/admin/<id>', methods=['PUT'])
@middleware(AuthMiddleware())
def update(id):
    return adminController.update(id)


@app.route(f'{url_prefix}/admin/<id>/password', methods=['PUT'])
@middleware(AuthMiddleware())
def update_password(id):
    return adminController.update_password(id)


@app.route(f'{url_prefix}/admin/<id>/activate', methods=['POST'])
@middleware(AuthMiddleware())
def activate(id):
    return adminController.activate(id)


@app.route(f'{url_prefix}/admin/<id>/activate', methods=['DELETE'])
@middleware(AuthMiddleware())
def deactivate(id):
    return adminController.deactivate(id)


@app.route(f'{url_prefix}/admin/<id>', methods=['DELETE'])
@middleware(AuthMiddleware())
def soft_delete(id):
    return adminController.soft_delete(id)


@app.route(f"{url_prefix}/admin/<id>/restore", methods=['POST'])
@middleware(AuthMiddleware())
def restore(id):
    return adminController.restore(id)


@app.route(f'{url_prefix}/admin/<id>/hard', methods=['DELETE'])
@middleware(AuthMiddleware())
def delete(id):
    return adminController.delete(id)
