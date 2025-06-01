senha_correta = "senha123"
tentativas = 0

while True:
    senha = input("Digite a senha: ")
    tentativas += 1

    if senha == senha_correta:
        print("Senha correta. Acesso concedido.")
        break
    elif tentativas == 3:
        print("Número máximo de tentativas atingido. Acesso bloqueado.")
        break
    else:
        print(f"Senha incorreta. Tentativa {tentativas}/3.")

