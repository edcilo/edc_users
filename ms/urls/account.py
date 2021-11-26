from ms import app
from ms.controllers import accountController
from ms.middlewares import middleware, AuthMiddleware


@app.route('/profile')
@middleware(AuthMiddleware)
def profile():
    return accountController.profile()
