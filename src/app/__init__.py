from flask import Flask
from flask_cors import CORS


def create_app():
  app = Flask(__name__)
  CORS(app)

  from .routes import actives
  app.register_blueprint(actives, url_prefix="/api")

  return app
