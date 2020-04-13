from . import db

class Active(db.Model):
  ticker = db.Column(db.String(10), primary_key=True)
  category = db.Column(db.String(10))
  price = db.Column(db.Float())

  def __init__(self, ticker, category, price):
    self.ticker = ticker
    self.category = category
    self.price = price