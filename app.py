from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL?sslmode=require')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

import routes, models