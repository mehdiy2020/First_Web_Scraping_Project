from locator_pkg.detail_locator import DetailParser

class DetailCurrencyParser:
  
  def __init__(self, parent):
    self.parent = parent
    
  def __repr__(self):
    return f"<The exchange rate for {self.currency_name} to Euro is {self.exchange_rate}"
    
  @property
  def currency(self):
    locator = DetailParser.CURRENCY
    img = self.parent.select_one(locator)
    return img['alt'].strip() if img else ''
  
  @property
  def currency_name(self):
    locator = DetailParser.CURRENCYNAME
    td = self.parent.select_one(locator)
    return td.get_text(strip=True) if td else ''
  
  @property
  def exchange_rate(self):
    locator = DetailParser.EXCAHGNERATE
    td = self.parent.select_one(locator).find('strong')
    return td.get_text(strip=True) if td else ''