from os import getenv
from dotenv import load_dotenv
load_dotenv()

def get_boolean(property):
  return getenv(property).lower() == 'true'

class Config:
  DEBUG = get_boolean('DEBUG')
  SQLALCHEMY_TRACK_MODIFICATIONS = get_boolean('SQLALCHEMY_TRACK_MODIFICATIONS')
  SECRET_KEY = getenv("SECRET_KEY")
  SQLALCHEMY_DATABASE_URI = getenv('DATABASE_URL')
