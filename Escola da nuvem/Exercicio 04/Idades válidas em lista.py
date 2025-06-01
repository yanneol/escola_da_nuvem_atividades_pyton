idades = []

while True:
    entrada = input("Digite uma idade ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break
    try:
        idade = int(entrada)
        if 0 <= idade <= 120:
            idades.append(idade)
        else:
            print("Idade inválida.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"Idades válidas: {idades}")
