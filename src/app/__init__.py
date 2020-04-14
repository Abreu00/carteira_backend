from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()
ma = Marshmallow()

app = Flask(__name__)

def create_app():
  CORS(app)
  app.config.from_object(Config)
  
  db.init_app(app)
  ma.init_app(app)

  from .routes import actives
  from .scrapper import schedule_scrapper

  app.register_blueprint(actives, url_prefix="/api")
  schedule_scrapper()

  return app