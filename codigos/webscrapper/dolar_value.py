import requests, json


# Função que busca o valor atual do dolar na moeda especificada 
# retorna uma tupla que contem:
# convertido para float, a data da cotacao, assim como o nome da moeada
def fetch_dolar_in_currency(currency_name = 'brl'): 

    response = requests.get('http://www.floatrates.com/daily/usd.json')

    currencies = response.json()

    try:
        choosed_currency = currencies[currency_name]
    except: 
        return None
        # Caso a chave passada nao exista no  json


    return (choosed_currency['name'],float(choosed_currency['rate']), choosed_currency['date'])
