def cadastrar_aluno():
    alunos = {}

    while True:
        nome = input("Nome do aluno (ou 'fim' para encerrar): ")
        if nome.lower() == 'fim':
            break

        notas = []
        for i in range(1, 4):
            while True:
                try:
                    nota = float(input(f"Digite a nota {i} para {nome}: "))
                    if 0 <= nota <= 10:
                        notas.append(nota)
                        break
                    else:
                        print("Nota inválida! Digite entre 0 e 10.")
                except ValueError:
                    print("Erro: digite um número válido.")

        alunos[nome] = notas

    return alunos

def calcular_media(notas):
    return sum(notas) / len(notas)

alunos = cadastrar_aluno()

if alunos:
    print("\nResultados:")
    maior_media = -1
    aluno_top = ""

    for nome, notas in alunos.items():
        media = calcular_media(notas)
        print(f"{nome}: média = {media:.2f}")
        if media > maior_media:
            maior_media = media
            aluno_top = nome

    print(f"\nAluno com a maior média: {aluno_top} ({maior_media:.2f})")
else:
    print("Nenhum aluno foi cadastrado.")
