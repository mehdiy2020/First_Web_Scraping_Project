from bs4 import BeautifulSoup

from locator_pkg.main_locator import OutterLocator
from parser_pkg.parser import DetailCurrencyParser

class GetMainHtml:
  def __init__(self, html):
    self.soup = BeautifulSoup(html, 'lxml')
    
  @property
  def main_content(self):
    locator = OutterLocator.MAINLOCATOR
    main_table = self.soup.select(locator)
    
    
    data_rows = [row for row in main_table[1:] if row.find('img', class_='flag')]
    return [DetailCurrencyParser(e) for e in  data_rows]


# import requests
# from bs4 import BeautifulSoup
# import re
# from pprint import pprint

# website_url = 'https://www.iban.com/exchange-rates'

# request = requests.get(url= website_url, headers={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
# }, timeout=10)
# html_content = request.content    
    
# all_content = BeautifulSoup(html_content, 'lxml').select('table.table-bordered.table-hover.downloads tbody tr')