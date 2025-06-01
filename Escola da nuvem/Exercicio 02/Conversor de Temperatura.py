temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F, K): ").upper()
destino = input("Converter para (C, F, K): ").upper()

def converter(t, de, para):
    if de == para:
        return t
    if de == "C":
        if para == "F":
            return t * 9/5 + 32
        elif para == "K":
            return t + 273.15
    elif de == "F":
        if para == "C":
            return (t - 32) * 5/9
        elif para == "K":
            return (t - 32) * 5/9 + 273.15
    elif de == "K":
        if para == "C":
            return t - 273.15
        elif para == "F":
            return (t - 273.15) * 9/5 + 32
    return None

resultado = converter(temp, origem, destino)

if resultado is not None:
    print(f"{temp}°{origem} = {resultado:.2f}°{destino}")
else:
    print("Conversão inválida.")
