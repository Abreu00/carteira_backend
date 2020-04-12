from flask import Flask
from flask_cors import CORS
from .routes import actives
from .config import Config
from .scrapper import schedule_scrapper

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(Config)
  schedule_scrapper()

  app.register_blueprint(actives, url_prefix="/api")

  return app