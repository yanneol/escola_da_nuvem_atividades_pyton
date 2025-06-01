pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para sair: ")
    if entrada.lower() == "fim":
        break
    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print("Par")
            pares += 1
        else:
            print("Ímpar")
            impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Digite um número inteiro.")

print(f"Pares: {pares} | Ímpares: {impares}")
