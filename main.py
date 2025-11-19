
import requests

  
from detail_pkg.top_down_content import GetMainHtml

website_url = 'https://www.iban.com/exchange-rates'

request = requests.get(url= website_url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}, timeout=10)
html_content = request.content

currency_information = GetMainHtml(html_content)

for outcome in currency_information.main_content:
  print(outcome.currency)
