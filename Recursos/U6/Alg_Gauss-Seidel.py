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

def gseidel(A,b,err,mit):
	M = np.tril(A)
	N = M - A
	x0 = np.zeros(b.shape)
	for k in range(mit):
		x1 = solvinf(M, N @ x0 + b)

		if np.linalg.norm( x1-x0 ,ord=np.inf) < err :
			break
		else:
			x0 = x1.copy()

	return [x1,k]