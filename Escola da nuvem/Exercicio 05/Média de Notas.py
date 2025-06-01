def calcular_media(notas):
    return sum(notas) / len(notas)

nome = input("Digite o nome do aluno: ")
notas = []

for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a nota {i}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("Erro: digite um número válido.")

media = calcular_media(notas)
print(f"A média do(a) aluno(a) {nome} é: {media:.2f}")
