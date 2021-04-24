from math import sqrt

def mala(a, b, c):
    disc = b**2-4*a*c
    if disc < 0:
        print("discriminante menor a 0, intente nuevamente")
        return None
    x_1 = (-b + sqrt(disc))/2*a
    x_2 = (-b - sqrt(disc))/2*a
    return [x_1, x_2]

def buena(a, b, c):
    disc = b**2-4*a*c
    if disc < 0:
        print("discriminante menor a 0, intente nuevamente")
        return None
    #buscaremos la raiz mas alejada en valor absoluto
    if b>0:
        x_1 = (-b - sqrt(disc))/2*a
    else:
        x_1 = (-b + sqrt(disc))/2*a
    
    x_2 = (c/a) / x_1

    return [x_1, x_2]