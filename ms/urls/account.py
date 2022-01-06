from ms import app
from ms.controllers import accountController
from ms.middlewares import middleware, AuthMiddleware


@app.route('/api/v1/users/profile')
@middleware(AuthMiddleware)
def profile():
    return accountController.profile()
