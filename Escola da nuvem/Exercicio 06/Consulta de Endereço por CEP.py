import requests

cep = input("Digite o CEP (apenas números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)
if response.status_code == 200:
    dados = response.json()
    if "erro" not in dados:
        print("Logradouro:", dados.get('logradouro', 'Não informado'))
        print("Bairro:", dados.get('bairro', 'Não informado'))
        print("Cidade:", dados.get('localidade', 'Não informado'))
        print("Estado (UF):", dados.get('uf', 'Não informado'))
    else:
        print("CEP não encontrado.")
else:
    print("Erro ao consultar o CEP.")
