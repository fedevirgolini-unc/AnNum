def horn(coefs, x):
    valor = 0
    for i in coefs:
        valor = i + x*valor
    return valor