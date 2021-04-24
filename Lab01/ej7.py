def potencia(x, n):
    pot = 1

    if n<0:
        base = (1/x)
        exp = -n
    else:
        base = x
        exp = n
    
    while exp>0:
        pot = base * pot
        exp = exp - 1
    
    return pot

num = int(input("Ingrese un numero: "))

for i in range(6):
    print(f"{num} elevado a la {i} es igual a: {potencia(num, i)}")
