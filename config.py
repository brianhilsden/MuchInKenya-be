from dotenv import load_dotenv
load_dotenv()
import os
from flask_migrate import Migrate
from flask import Flask,session
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api,Resource
from flask import request, session,make_response
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///munchinkenya.db"
""" app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI') """
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
db = SQLAlchemy()
migrate = Migrate(app, db)
db.init_app(app)

bcrypt = Bcrypt(app)

api = Api(app)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})