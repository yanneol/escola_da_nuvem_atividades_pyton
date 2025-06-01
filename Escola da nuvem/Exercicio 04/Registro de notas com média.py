notas = []

while True:
    entrada = input("Digite uma nota de 0 a 10 ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota fora do intervalo.")
    except ValueError:
        print("Entrada inválida.")

if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")
