import asyncio
from typing import List
from async_request import AsyncRequest

class Stock:
  def __init__(self, symbol: str , jsonData: dict) -> None:
    self.symbol = symbol
    self.current_price = jsonData["c"]
    self.change = jsonData["d"]
    self.percent_change = jsonData["dp"]
    self.today_high_price = jsonData["h"]
    self.today_low_price = jsonData["l"]
    self.today_open_price = jsonData["o"]
    self.previous_close_price = jsonData["c"]


class StockApiClient :
  def __init__(self, api_key: str, request= AsyncRequest()) -> None:
    self.__base_url = "https://finnhub.io/api/v1/quote?token=" + api_key
    self.__request = request
  
  def get_stocks(self, *symbols: str) -> List[Stock]:
    urls = [self.__symbol_to_url(symbol) for symbol in symbols]
    responses = asyncio.run(self.__request.get_all(*urls))
    return [
      Stock(jsonData=response, symbol=symbols[idx]) for idx, response in enumerate(responses)
    ]
  
  def __symbol_to_url(self, symbol: str) -> str:
    return self.__base_url + "&symbol="+ symbol

