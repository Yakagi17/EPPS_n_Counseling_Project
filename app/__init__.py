from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate, MigrateCommand, Manager
from flask_login import LoginManager, UserMixin

app = Flask(__name__)


#Database
app.config.from_object(Config)
db = SQLAlchemy(app)

# Not migrated yet.
# migrate = Migrate(app, db)

#Login config later
# login = LoginManager(app)
# login.login_view = 'login'
# login.login_message_category = 'info'