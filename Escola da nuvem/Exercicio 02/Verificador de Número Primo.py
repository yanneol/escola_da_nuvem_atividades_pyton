num = int(input("Digite um número inteiro positivo: "))

if num < 2:
    print("Não é primo.")
else:
    primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
            break
    if primo:
        print("É um número primo.")
    else:
        print("Não é primo.")
