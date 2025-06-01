numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numeros:
    if num < 2:
        continue
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(f"{num} é primo")
