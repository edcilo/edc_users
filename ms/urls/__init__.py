from flask import jsonify
from ms import app
from .auth import *
from .admin import *
from .account import *


url_prefix = app.config.get('URL_PREFIX')

@app.route(f"{url_prefix}/about")
def about():
    return jsonify({
        "data": {
            "name": app.config.get('APP_NAME'),
            "version": app.config.get('APP_VERSION'),
        },
        "code": 200
    }), 200
