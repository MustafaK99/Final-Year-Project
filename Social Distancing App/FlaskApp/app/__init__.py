from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import dataScraper

app = Flask(__name__)
app.config['SECRET_KEY'] = '6e42af73537c607675cb4cc78e3959e8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from app import routes
