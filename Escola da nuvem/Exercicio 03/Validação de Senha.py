senha_correta = "1234"

while True:
    senha = input("Digite a senha: ")
    if senha == senha_correta:
        print("Acesso concedido.")
        break
    else:
        print("Senha incorreta. Tente novamente.")
