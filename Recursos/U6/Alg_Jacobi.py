import numpy as np

def jacobi(A,b,err,mit):
	M = np.diag(np.diag(A))
	N = M - A
	M_inv = np.diag(1/np.diag(M))
	x0 = np.zeros(b.shape)
	for k in range(mit):
		x1 = M_inv @ N @ x0 + M_inv @ b

		if np.linalg.norm( x1-x0 ,ord=np.inf) < err :
			break
		else:
			x0 = x1.copy()

	return [x1,k]