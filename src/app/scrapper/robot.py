from bs4 import BeautifulSoup
import requests

map_type_url = {
  'stock': 'acoes',
  'etf': 'etfs',
  'fii': 'fundos-imobiliarios'
}

class Robot:
  base_url='https://statusinvest.com.br'

  def __init__(self, active):
    print(f'Updating price of {active.ticker}')
    url = f'{Robot.base_url}/{map_type_url[active.category]}'
    url += '/' + active.ticker
    self.url = url
    self.active = active

  def update(self):
    req = requests.get(self.url)
    soup = BeautifulSoup(req.text, 'lxml')
    price_txt = soup.find('div', class_='top-info').find('strong').text
    price = float(price_txt.replace(',', '.'))
    self.active.price = price
