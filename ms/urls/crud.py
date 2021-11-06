from ms import app
from ms.controllers import userController
from ms.middlewares import auth


@app.route('/')
@auth.auth
def list(jwt_payload):
    return userController.list()


@app.route('/', methods=['POST'])
@auth.auth
def create(jwt_payload):
    return userController.create()


@app.route('/<id>')
@auth.auth
def detail(id, jwt_payload):
    return userController.detail(id)


@app.route('/<id>', methods=['PUT'])
@auth.auth
def update(id, jwt_payload):
    return userController.update(id)


@app.route('/<id>', methods=['DELETE'])
@auth.auth
def soft_delete(id, jwt_payload):
    return userController.soft_delete(id)


@app.route('/<id>/hard', methods=['DELETE'])
@auth.auth
def delete(id, jwt_payload):
    return userController.delete(id)
