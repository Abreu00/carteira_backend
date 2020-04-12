from apscheduler.schedulers.background import BackgroundScheduler
import atexit
import os

def func():
  print('oi')

def create_scheduler():
  if os.getenv('DEBUG').lower() != 'true' or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
    sched = BackgroundScheduler(daemon=True)
    sched.add_job(func,'interval',minutes=1)
    sched.start()

    atexit.register(lambda: sched.shutdown(wait=True))