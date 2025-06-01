def main():
    nome = input("Digite seu nome: ")
    try:
        idade = int(input("Digite sua idade: "))
        print(f"Olá, {nome}! Você tem {idade} anos.")
    except ValueError:
        print("Erro: idade inválida.")

if __name__ == "__main__":
    main()
