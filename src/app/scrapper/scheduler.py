from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os
from .robot import Robot
from ..db import actives_list

def update_actives():
  for active in actives_list:
    bot = Robot(active['ticker'], active['type'])
    print('start')
    bot.update()
    print('end')

def schedule_scrapper():
  if os.getenv('DEBUG').lower() != 'true' or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(update_actives, 'interval', minutes=1)
    sched.start()
    atexit.register(lambda: sched.shutdown(wait=True))