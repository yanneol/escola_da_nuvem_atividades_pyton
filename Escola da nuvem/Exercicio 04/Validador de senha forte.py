while True:
    senha = input("Digite uma senha forte (mín. 8 caracteres e 1 número) ou 'sair': ")
    if senha.lower() == "sair":
        break
    if len(senha) >= 8 and any(char.isdigit() for char in senha):
        print("Senha válida!")
        break
    else:
        print("Senha fraca. Tente novamente.")
