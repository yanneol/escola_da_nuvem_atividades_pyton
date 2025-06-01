from datetime import datetime

def calcular_idade_em_dias(ano_nascimento):
    ano_atual = datetime.now().year
    return (ano_atual - ano_nascimento) * 365

try:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_atual = datetime.now().year
    if ano_nascimento > ano_atual:
        print("Erro: o ano de nascimento não pode ser maior que o ano atual.")
    else:
        idade_dias = calcular_idade_em_dias(ano_nascimento)
        print(f"Você tem aproximadamente {idade_dias} dias de vida.")
except ValueError:
    print("Erro: digite um ano válido.")
