import requests, json


# Função que busca o valor atual do dolar em reais 
# e retorna convertido para float, assim como a data da cotacao
def fetch_dolar_currency(): 

    response = requests.get('http://www.floatrates.com/daily/usd.json')

    currencies = response.json()

    brl_currency = currencies['brl']

    return float(brl_currency['rate']), brl_currency['date']




