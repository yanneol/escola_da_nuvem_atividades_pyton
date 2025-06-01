compras = []

while len(compras) < 10:
    try:
        item = input("Digite o nome de um produto (ou 'fim' para encerrar): ")
        if item == "":
            continue
        if item.lower() == "fim":
            break
        compras.append(item)
    except Exception:
        print("Erro ao registrar item. Tente novamente.")

print("Lista de compras:", compras)
