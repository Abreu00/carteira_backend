from os import getenv
from dotenv import load_dotenv
load_dotenv()

class Config:
  DEBUG=getenv('DEBUG').lower() == 'true'
  SECRET_KEY=getenv("SECRET_KEY")