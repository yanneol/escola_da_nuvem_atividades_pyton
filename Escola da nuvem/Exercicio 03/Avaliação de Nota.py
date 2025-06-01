nota = float(input("Digite a nota (0 a 10): "))

if nota < 5:
    print("Reprovado")
elif nota < 7:
    print("Em recuperação")
else:
    print("Aprovado")
