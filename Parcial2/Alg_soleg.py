import numpy as np

def soltrsup(A, b):
    n = A.shape[0]
    x = b

    for idx in range(n-1, -1, -1):
        for jdx in range(n-1, idx, -1):
            x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

def egauss(A_, b_):

    A = A_.copy()
    b = b_.copy()
    n = A.shape[0]

    for k in range(n-1):
        for i in range(k+1,n):
            if A[k,k] == 0:
                print('El elemento a_kk es igual a cero.')
                return None
            
            m = A[i,k] / A[k,k]

            for j in range(k,n):
                A[i,j] = A[i,j] - m * A[k,j]    
            b[i] = b[i] - m * b[k]

    return A, b

def soleg(A,b):
    U, y = egauss(A,b)
    x = soltrsup(U,y)
    return x