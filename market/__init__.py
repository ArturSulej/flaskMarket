from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # Initialize Flask, get local python file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'   # Add extra configuration to allow app locate database
app.config['SECRET_KEY'] = '838cf2d042d04baf3eda70a6'
db = SQLAlchemy(app)   # Instance of SQLAlchemy class

from market import routes
