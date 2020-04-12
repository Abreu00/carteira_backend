from bs4 import BeautifulSoup
import requests

class Robot:
  base_url='https://statusinvest.com.br'

  def __init__(self, ticker, active_type):
    url = f'{Robot.base_url}/acoes' if active_type == 'stock' else f'{Robot.base_url}/fundos-imobiliarios'
    url += '/' + ticker
    self.url = url

  def update(self):
    req = requests.get(self.url)
    soup = BeautifulSoup(req.text, 'lxml')
    price_txt = soup.find('div', class_='top-info').find('strong').text
    self.price = float(price_txt.replace(',', '.'))
    print(self.price)
    print(type(self.price))
