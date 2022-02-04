from ms import app
from ms.controllers import AccountController
from ms.middlewares import middleware, AuthMiddleware


url_prefix = app.config.get('URL_PREFIX')


@app.route(f'{url_prefix}/profile')
@middleware(AuthMiddleware())
def profile():
    return AccountController().profile()
