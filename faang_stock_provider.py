from stock_api import StockApiClient

class FaangStockProvider:
  apple_symbol = "AAPL"
  amazon_symbol = "AMZN"
  facebook_symbol = "META"
  netflix_symbol = "NFLX"
  google_symbol = "GOOGL"

  def __init__(self, stock_api: StockApiClient) -> None:
    self.__stock_api = stock_api

  def stocks(self):
    return self.__stock_api.get_stocks(
      self.apple_symbol,
      self.amazon_symbol,
      self.facebook_symbol,
      self.netflix_symbol,
      self.google_symbol,
    )

  def most_volatile_stock(self):
    stocks =  self.stocks()
    return max(stocks, key=lambda stock: stock.change)

  