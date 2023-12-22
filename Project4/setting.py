from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://sql5667235:viLq8NBU13@sql5.freemysqlhosting.net/sql5667235"
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1111@127.0.0.1/mysql"
db = SQLAlchemy(app)

socketio = SocketIO(app)