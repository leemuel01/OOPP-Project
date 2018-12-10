from flask import Flask
from flask_sqlalchemy import SQLAlchemy #database stuff
from flask_bcrypt import Bcrypt #password encryption stuff
from flask_login import LoginManager #Login stuff
app = Flask(__name__)

#Security stuff so no cookie configuration
app.config["SECRET_KEY"] = '49dc263f9ebdbf0510c9273e5320e7df'

#Database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///site.db"
db = SQLAlchemy(app)

#Password encryption
bcrypt = Bcrypt()

#Login management
login_manager = LoginManager(app)

#Login required
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Flask import routes