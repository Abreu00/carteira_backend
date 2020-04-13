from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config
from .scrapper import schedule_scrapper

db = SQLAlchemy()

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(Config)
  
  db.init_app(app)

  schedule_scrapper()

  from .routes import actives

  app.register_blueprint(actives, url_prefix="/api")

  return app