from flask import Flask
from flask_cors import CORS
from .config import Config
from .scheduler import create_scheduler

app = Flask(__name__)

def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config.from_object(Config)
  create_scheduler()

  from .routes import actives
  app.register_blueprint(actives, url_prefix="/api")

  return app
