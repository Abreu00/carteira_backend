from app import create_app, db
from app.models import Active
from app.scrapper.scheduler import update_actives
from supported import supported_fiis, supported_stocks

app = create_app()

#Creates all Tables used by the app
def create_all():
  with app.app_context():
    db.create_all()

#Drops all Tables used by the app
def drop_all():
  with app.app_context():
    db.drop_all()

#Creates initial set of actives to be maintened by the api
def create_initial_set():
  with app.app_context():
    actives = []
    for active in supported_stocks:
      new_active = Active(active, 'stock', 1)
      actives.append(new_active)
    for active in supported_fiis:
      new_active = Active(active, 'fii', 1)
      actives.append(new_active)
    db.session.bulk_save_objects(actives)
    db.session.commit()

def add_active(ticker, category, price):
  with app.app_context():
    new_active = Active(ticker, category, price)
    db.session.add(new_active)
    db.session.commit()

#Updates prices of actives on database
def force_update():
  update_actives()

