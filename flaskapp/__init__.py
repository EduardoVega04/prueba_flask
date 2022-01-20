from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import logging
from logging import FileHandler
import pytz


app = Flask(__name__)
app.config['SECRET_KEY'] = '88ca1a7bfe8acc934332c4c470a29eab'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Configure the logger
file_handler = FileHandler('usersLog.log')
file_handler.setLevel(logging.INFO)
app.logger.addHandler(file_handler)

# Get Colombian timezone for logging purposes
cot = pytz.timezone('America/Bogota')


# In the python shell, type:
# from flaskapp import db
# db.create_all()
db = SQLAlchemy(app)


from flaskapp import routes
