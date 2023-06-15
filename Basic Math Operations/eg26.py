import numpy
import scipy.sparse
a=numpy.matrix(((0,0,0,24),(0,19,0,0),(0,0,0,1),(14,0,0,1),(0,-1,0,11),(0,0,0,71)))
print('a\n',a)
k=numpy.count_nonzero(a)
print('Non zeros count:',k)
sh=a.shape
rows=a.shape[0]
cols=a.shape[1]
print('Rows:',rows)
print('Cols:',cols)
sz=a.size
print('Size:',sz)
x=1-(k/sz)
print('Scipy issparse():',scipy.sparse.issparse(scipy.sparse.csr_matrix(a)))
if x>0.5:
    print('True')
else:
    print('False')