from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS


load_dotenv()
app = Flask(__name__)
CORS(app)


import ms.config
import ms.config
import ms.urls
import ms.models
