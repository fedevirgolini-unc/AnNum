from ej3 import rnewton

def kmh_ms(x):
    return x * 0.277

def diametro(d, vel, en):
    f = 0.01328 * d**2 * vel**3 - en
    df = 0.01328 * 2 * d * vel**3
    return f, df

def det_diametro(energia, velocidad):

    auxiliar = lambda d : diametro(d, velocidad, energia)

    hx, hf = rnewton(auxiliar, 1, 1e-5, 100)

    diam = hx[-1]
    return diam

print(f"El diametro debe ser de: {det_diametro(500,  kmh_ms(24))}")