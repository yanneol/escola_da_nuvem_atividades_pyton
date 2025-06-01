positivos = []
negativos = []

while True:
    entrada = input("Digite um número inteiro ou '0' para encerrar: ")
    if entrada == "0":
        break
    try:
        num = int(entrada)
        if num > 0:
            positivos.append(num)
        elif num < 0:
            negativos.append(num)
    except ValueError:
        print("Entrada inválida.")

print(f"Positivos: {len(positivos)} | Negativos: {len(negativos)}")
