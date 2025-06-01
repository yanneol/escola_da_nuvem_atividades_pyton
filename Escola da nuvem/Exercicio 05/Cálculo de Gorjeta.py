def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)

try:
    valor = float(input("Digite o valor da conta: "))
    porcentagem = float(input("Digite a porcentagem de gorjeta: "))
    gorjeta = calcular_gorjeta(valor, porcentagem)
    print(f"Gorjeta: R${gorjeta:.2f}")
except ValueError:
    print("Erro: digite valores numéricos válidos.")
