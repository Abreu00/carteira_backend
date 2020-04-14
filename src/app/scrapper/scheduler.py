from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os
from .. import app, db
from .robot import Robot
from ..models import Active

def update_actives():
  with app.app_context():
    actives = Active.query.all()
    for active in actives:
      bot = Robot(active)
      bot.update()
    db.session.commit()
    print('Updated actives succesfully')

def schedule_scrapper():
  if os.getenv('DEBUG').lower() != 'true' or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(update_actives, 'interval', hours=24)
    sched.start()
    atexit.register(lambda: sched.shutdown(wait=True))