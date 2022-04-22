from flask import Blueprint


api = Blueprint('api', __name__, url_prefix="/api/v1/users")
web = Blueprint('web', __name__, url_prefix="/")
