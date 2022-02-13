from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

app = Flask(__name__)

app.config["SECRET_KEY"] = '710eb8ea461aea8b8b7f12f42c67b3f8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.permanent_session_lifetime = timedelta(minutes=30)
from project import routes
