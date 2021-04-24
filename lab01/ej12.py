def SonOrtogonales(x, y):
    prod = x[0]*y[0]+x[1]*y[1]
    return 0 == prod

x = [1, 1.1024074512658109]
y = [-1, 1/x[1]]

if not SonOrtogonales(x, y):
    print("Algo saliño mal...")