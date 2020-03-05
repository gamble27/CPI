import re
import pandas as pd
from urllib.request import urlopen
import datetime
from monthdelta import monthdelta


def get_exchange_rate():
    r = r'Долар США.+?\n.+?\n.+?(?P<nbu>\d+?.\d+?)<'
    url1 = 'https://bank.gov.ua/markets/exchangerates/?date='
    url2 = '&period=daily'
    date = datetime.datetime.strptime('2007-02-01', '%Y-%m-%d')
    res = {}
    dates = ''
    month = monthdelta(1)
    while dates != '01.06.2019':
        date = date + month
        dates = date.strftime('%d.%m.%Y')
        print(dates)
        request = urlopen(url1 + dates + url2)
        c = list(re.finditer(r, str(request.read(), encoding='utf-8', errors='ignore')))
        try:
            curs = float('.'.join(c[0].group('nbu').split(',')))
            if curs > 500:
                curs = curs/100
        except Exception:
            curs = 0
        res[date] = curs
    res = pd.DataFrame.from_dict(res, orient='index', columns=['UAH/USD'])
    res.index = res.index.to_period(freq='M')
    res.to_csv('curs.csv')


if __name__ == "__main__":
    get_exchange_rate()
