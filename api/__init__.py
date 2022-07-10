from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import logging

app = Flask(__name__)
app.config.from_object('app_config')

db = SQLAlchemy(app)
mashmallow = Marshmallow(app)

from .models import *
from .routes import index, organization, user
from .tools.DataHandler import DataHandler

data_handler = DataHandler('./api/data', ['organization.csv', 'user.csv'])