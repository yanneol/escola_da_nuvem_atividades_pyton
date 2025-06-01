nota = int(input("Avalie o restaurante (0 a 5): "))

if nota == 5:
    print("★★★★★ - Excelente! Muito obrigado pela avaliação.")
elif nota == 4:
    print("★★★★☆ - Muito bom! Ficamos felizes com sua satisfação.")
elif nota == 3:
    print("★★★☆☆ - Bom! Vamos buscar melhorar ainda mais.")
elif nota == 2:
    print("★★☆☆☆ - Precisamos melhorar. Obrigado pelo feedback.")
elif nota == 1:
    print("★☆☆☆☆ - Lamentamos a experiência. Vamos melhorar.")
elif nota == 0:
    print("☆☆☆☆☆ - Que pena! Vamos trabalhar para evoluir.")
else:
    print("Nota inválida. Digite um número de 0 a 5.")
