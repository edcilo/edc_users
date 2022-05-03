from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


import ms.config
import ms.commands
import ms.db
import ms.db.cache
import ms.models
import ms.routes
