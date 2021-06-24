from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://husysxlukvwsek:5ca6d009c546bc0d3e725fc77008899754588d5674150a4e771c49ff07b9801e@ec2-34-193-112-164.compute-1.amazonaws.com:5432/daasknvfvi0nth" or 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login = LoginManager(app)
login.login_view = 'login'

import routes, models