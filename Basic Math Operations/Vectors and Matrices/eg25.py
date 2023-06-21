import numpy
import scipy.sparse
a=numpy.matrix(((0,0,0,24),(0,19,0,0),(0,0,0,1),(14,0,0,1),(0,-1,0,11),(0,0,0,71)))
print('a\n',a)
ca=scipy.sparse.csr_matrix(a)
print('compressed form\n',ca)
print(scipy.sparse.issparse(ca))
print(scipy.sparse.issparse(a))    # This will give always false, issparse() function takes argument as "csr_matrix" not ndarray
