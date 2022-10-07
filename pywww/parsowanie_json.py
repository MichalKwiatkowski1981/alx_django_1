import json
import requests
SZABLON_URL = 'http://api.nbp.pl/api/exchangerates/rates/c/{}/2016-04-04/?format=json'
waluta = input('Podaj walutę: ')
r = requests.get(SZABLON_URL.format(waluta))
# j_s = r.text
# j = json.loads(j_s)
# print(r.status_code)
r.raise_for_status()
j = r.json()
print(j['rates'][0]['bid'])
requests.get('http://api.nbp.pl/api/exchangerates/rates/c/usd/2016-04-04/?format=json').json()['rates'][0]['bid']


#używamy antualnej ceny średniej z API NBP
SZABLON_URL = 'http://api.nbp.pl/api/exchangerates/rates/c/{}/2016-04-04/?format=json'
def policz_koszyk(koszyk):
    return 4444.67

if __name__ == '__main__':
    k = {
        'usd': 34,
        'chf': 123,
        'eur': 555
    }
    print('Suma:', policz_koszyk(k))
