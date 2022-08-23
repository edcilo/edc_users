from ms.controllers import ApiController
from .blueprints import api
from .apiRoutes.account import *
from .apiRoutes.auth import *
from .apiRoutes.admin import *
from .apiRoutes.permissions import *
from .apiRoutes.roles import *
from .apiRoutes.shopper import *
from .apiRoutes.app import *


@api.route('/')
def api_index():
    return ApiController.action('index')
