# importing necessary modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# creating intances
app = Flask(__name__)
app.config.from_object("config")
db = SQLAlchemy(app)

# importing routes
from app import routes
