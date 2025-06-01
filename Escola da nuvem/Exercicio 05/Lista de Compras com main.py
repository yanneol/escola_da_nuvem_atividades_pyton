def main():
    lista_compras = []
    print("Digite os itens da lista de compras (digite 'fim' para encerrar):")

    while len(lista_compras) < 10:
        try:
            item = input("Item: ").strip()
            if item.lower() == "fim":
                break
            elif item == "":
                continue
            else:
                lista_compras.append(item)
        except Exception:
            print("Erro: insira apenas textos válidos.")

    print("\nItens na lista de compras:")
    for i, item in enumerate(lista_compras, 1):
        print(f"{i}. {item}")

if __name__ == "__main__":
    main()
