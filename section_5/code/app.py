from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_jwt import JWT
import datetime

# import the security settings for logIN
from security import authenticate, identity

# import the settings
from settings import *

# Local_settings override settings
try:
    from local_settings import *
except ImportError:
    pass

# Import others models
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = APP_KEY
api = Api(app)

# JWT config
# app.config['JWT_AUTH_URL_RULE'] = AUTH_URL_PATH

app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(
    seconds=EXPIRATION_TIME)

# /auth (the instance create a new endpoint)
jwt = JWT(app, authenticate, identity)

# Routes
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

# with this syntax you can run the server only with this command : python app.py
app.run(port=5000, debug=True)
