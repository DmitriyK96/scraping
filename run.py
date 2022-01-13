import sqlite3
from sys import argv
from getDownloadData import *

print("start download")

name = argv[1]
data = get_data(name)

connection = sqlite3.connect("currency.db")
ExchangeRates = BdExchangeRates(connection)
ExchangeRates.insert(data)

print("{0} rows loaded".format(len(data)))
ExchangeRates.close_connection()
print("end download")
