palavras_longas = []

while True:
    try:
        palavra = input("Digite uma palavra (ou 'parar'): ")
        if palavra.lower() == "parar":
            break
        if palavra.isnumeric():
            continue
        if len(palavra) > 5:
            palavras_longas.append(palavra)
    except Exception:
        print("Erro ao processar entrada.")

print("Palavras com mais de 5 letras:", palavras_longas)
