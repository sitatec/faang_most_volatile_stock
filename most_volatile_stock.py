import csv
from stock_api import StockApiClient
from faang_stock_provider import FaangStockProvider

def write_to_csv(rows: list, filename = "most_volatile_stock.csv"):
  with open(filename, "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)


if __name__ == '__main__':
  # You may need to replace the api_key
  client = StockApiClient(api_key="cdgpu5iad3i2r375edggcdgpu5iad3i2r375edh0")
  faang_stock = FaangStockProvider(client)
  most_volatile_stock = faang_stock.most_volatile_stock()
  csv_header = ["stock_symbol","percentage_change","current_price","last_close_price"]
  csv_row = [most_volatile_stock.symbol, most_volatile_stock.percent_change, most_volatile_stock.current_price, most_volatile_stock.previous_close_price]
  write_to_csv([csv_header, csv_row])
