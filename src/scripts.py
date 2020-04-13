from app import create_app, db
from app.models import User

app = create_app()

def create_all():
  with app.app_context():
    db.create_all()

def drop_all():
  with app.app_context():
    db.drop_all()

