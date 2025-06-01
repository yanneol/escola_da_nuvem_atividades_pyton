temperaturas = []

while len(temperaturas) < 7:
    entrada = input("Digite a temperatura (Celsius) ou 'fim': ")
    if entrada.lower() == "fim":
        break
    try:
        temp = float(entrada)
        temperaturas.append(temp)
    except ValueError:
        print("Temperatura inválida.")

if temperaturas:
    media = sum(temperaturas) / len(temperaturas)
    print(f"Média das temperaturas: {media:.2f}°C")
else:
    print("Nenhuma temperatura válida foi registrada.")
