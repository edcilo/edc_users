from ms import app
from ms.controllers import userController
from ms.middlewares import middleware, AuthMiddleware


@app.route('/')
@middleware(AuthMiddleware)
def list():
    return userController.list()


@app.route('/', methods=['POST'])
@middleware(AuthMiddleware)
def create():
    return userController.create()


@app.route('/<id>')
@middleware(AuthMiddleware)
def detail(id):
    return userController.detail(id)


@app.route('/<id>', methods=['PUT'])
@middleware(AuthMiddleware)
def update(id):
    return userController.update(id)


@app.route('/<id>/activate', methods=['POST'])
@middleware(AuthMiddleware)
def activate(id):
    return userController.activate(id)


@app.route('/<id>/activate', methods=['DELETE'])
@middleware(AuthMiddleware)
def deactivate(id):
    return userController.deactivate(id)


@app.route('/<id>', methods=['DELETE'])
@middleware(AuthMiddleware)
def soft_delete(id):
    return userController.soft_delete(id)


@app.route("/<id>/restore", methods=['POST'])
@middleware(AuthMiddleware)
def restore(id):
    return userController.restore(id)


@app.route('/<id>/hard', methods=['DELETE'])
@middleware(AuthMiddleware)
def delete(id):
    return userController.delete(id)
