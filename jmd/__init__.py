from flask import Flask
from flask.ext.admin import Admin
from flask.ext.bcrypt import Bcrypt
from flask.ext.login import LoginManager
from flask.ext.mongoengine import MongoEngine

from jmd.config import config

app = Flask(__name__)
app.config.from_object(config)

# Jinja Prettiness
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

# Extensions
admin = Admin(app)
crypt = Bcrypt(app)
db = MongoEngine(app)
login_manager = LoginManager(app)

# Import the MVC elements
import jmd.view
import jmd.view.admin
import jmd.model.login
import jmd.control.filters
