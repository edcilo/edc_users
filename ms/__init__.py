from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=[
    "(^(http|https):\/\/)(.*)(edcilo.com)",
    "https://edc-dashboard-pi.vercel.app",
    "http://localhost:3000"
])


import ms.config
import ms.commands
import ms.db
import ms.db.cache
import ms.models
import ms.routes
