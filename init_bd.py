import sqlite3

connection = sqlite3.connect('currency.db')
cur = connection.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS EXCHANGE_RATES(
    NAME TEXT,
    DATE TEXT,
    VALUE REAL)""")

connection.close()
print('Ok')

