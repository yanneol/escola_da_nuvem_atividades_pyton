pares = []

while True:
    try:
        numero = int(input("Digite 10 números inteiros. Apenas os pares válidos serão armazenados. Digite um número: "))
        if numero % 2 == 0:
            pares.append(numero)
            print(f"Número par aceito: {numero} (Total: {len(pares)}/10)")
            if len(pares) == 10:
                break
        else:
            print("Número ímpar. Tente novamente.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

print(f"\nNúmeros pares válidos: {pares}")