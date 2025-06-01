paises = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio",
    "Canadá": "Ottawa"
}

pais = input("Digite o nome de um país: ")
capital = paises.get(pais)

if capital:
    print(f"A capital de {pais} é {capital}.")
else:
    print("País não encontrado.")
