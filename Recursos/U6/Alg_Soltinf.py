import numpy as np

def solvinf(A,b):
    
    if np.linalg.det(A) == 0 :
        print("Matriz singular!")
        return None
    
    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n):
        x[i] = b[i] - np.dot(A[i, :i], x[:i])
        x[i] = x[i] / A[i,i]
    
    return x