import requests
from lxml import html
import datetime



def get_data(name):
    name = name.replace('-', ' ')
    url_base = 'https://cbr.ru/currency_base/daily/?UniDbQuery.Posted=True&UniDbQuery.To='
    min_date = '01.07.1992'
    date_obj = datetime.datetime.strptime(min_date, '%d.%m.%Y')
    date_now_obj = datetime.datetime.now()
    data = []
    while True:
        date_str = date_obj.strftime('%d.%m.%Y')
        # print(date_str)\
        r = requests.get(url_base + date_str)
        tree = html.fromstring(r.text.encode('UTF8'))
        result = tree.xpath("//tbody/*")
        for i in range(len(result) - 1):
            if result[i][3].text == name:
                data.append((name, date_str, result[i][4].text))
                break
        date_obj = date_obj + datetime.timedelta(days=1)

        if date_obj > date_now_obj:
            break


    return data

class BdExchangeRates:
    def __init__(self, con):
        self._connection = con
        self._cur = self._connection.cursor()

    def insert(self, data):
        self._cur = self._connection.cursor()
        self._cur.executemany("""INSERT INTO EXCHANGE_RATES VALUES(?, ?, ?);""", data)
        self._connection.commit()

    def close_connection(self):
        self._connection.close()

    def select_all(self, n):
        self._cur.execute("""SELECT * FROM EXCHANGE_RATES;""")
        return self._cur.fetchmany(n)

    def delete_all(self):
        self._cur.execute("""DELETE FROM EXCHANGE_RATES;""")
        self._connection.commit()
