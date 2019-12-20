from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from personal_website.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# tells the login_manager where the login is
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# to prevent circular import, we import at the end of the file
from personal_website import routes
