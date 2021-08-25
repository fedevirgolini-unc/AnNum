from scipy import linalg
import numpy as np

def soltrinf(A,b):

    if np.linalg.det(A) == 0 :
        print('La matriz es singular')
        return None

    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n):
        x[i] = b[i] - np.dot( A[i,:i ], x[:i] )
        x[i] = x[i] / A[i,i]

    return x 

def soltrsup(A, b):
    n = A.shape[0]
    x = b

    for idx in range(n-1, -1, -1):
        for jdx in range(n-1, idx, -1):
            x[idx] = x[idx] - A[idx, jdx] * x[jdx]
        x[idx] = x[idx] / A[idx, idx]

    return x

def sollu(A, b):
    P, L, U = linalg.lu(A)
    y = P.T @ b
    z = soltrinf(L, y)
    x = soltrsup(U, z)

    return x