from ms import app
from ms.controllers import AdminController
from ms.middlewares import middleware, AuthMiddleware, RoleMiddleware


url_prefix = app.config.get('URL_PREFIX')


@app.route(f'{url_prefix}/admin')
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def list():
    return AdminController().list()


@app.route(f'{url_prefix}/admin', methods=['POST'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def create():
    return AdminController().create()


@app.route(f'{url_prefix}/admin/<id>')
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def detail(id):
    return AdminController().detail(id)


@app.route(f'{url_prefix}/admin/<id>', methods=['PUT'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def update(id):
    return AdminController().update(id)


@app.route(f'{url_prefix}/admin/<id>/password', methods=['PUT'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def update_password(id):
    return AdminController().update_password(id)


@app.route(f'{url_prefix}/admin/<id>/activate', methods=['POST'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def activate(id):
    return AdminController().activate(id)


@app.route(f'{url_prefix}/admin/<id>/activate', methods=['DELETE'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def deactivate(id):
    return AdminController().deactivate(id)


@app.route(f'{url_prefix}/admin/<id>', methods=['DELETE'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def soft_delete(id):
    return AdminController().soft_delete(id)


@app.route(f"{url_prefix}/admin/<id>/restore", methods=['POST'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def restore(id):
    return AdminController().restore(id)


@app.route(f'{url_prefix}/admin/<id>/hard', methods=['DELETE'])
@middleware(AuthMiddleware())
@middleware(RoleMiddleware('admin'))
def delete(id):
    return AdminController().delete(id)
