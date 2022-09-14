import requests
import json

lista = {
    "BTC": 0,"ETH": 0,"DOT": 0,"MATIC": 0,"LINK": 0,"AVAX": 0,"FTT": 0,"CRO": 0,"CHZ": 0,"ADA": 0
    }

capital = 1500/len(lista)
url = "https://api.binance.com/api/v3/ticker/price"
payload = ""

for row in lista:
    querystring = {"symbol":f"{row}USDT"}    
    response = requests.request("GET", url, data=payload, params=querystring)
    resposta = json.loads(response.text)
    try: 
        preco = float(resposta["price"])
        quantidade = capital/preco
        print(f'Criptomoeda {row} preço atual é R$ {round(preco,2)} - R$ {round(capital,2)} p/ Empregar dá {round(quantidade,3)} UNDs')
    except:
        print(f'Criptomoeda {row} preço sem cotação')