import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

response = requests.get(url)
if response.status_code == 200:
    dados = response.json()
    chave = f"{moeda}BRL"
    if chave in dados:
        cotacao = dados[chave]
        print("Moeda:", cotacao['code'])
        print("Valor atual (R$):", cotacao['bid'])
        print("Valor máximo (R$):", cotacao['high'])
        print("Valor mínimo (R$):", cotacao['low'])
        print("Data e hora da atualização:", cotacao['create_date'])
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar a API.")
