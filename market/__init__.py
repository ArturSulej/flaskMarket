from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)  # Initialize Flask, get local python file name
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'   # Add extra configuration to allow app locate database
app.config['SECRET_KEY'] = '838cf2d042d04baf3eda70a6'
db = SQLAlchemy(app)   # Instance of SQLAlchemy class
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = 'warning'

from market import routes
