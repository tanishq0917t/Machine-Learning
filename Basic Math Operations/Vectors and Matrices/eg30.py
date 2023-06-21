import numpy
import scipy.sparse
a=numpy.matrix(((0,0,0,1),(1,0,0,1),(1,0,1,0),(1,0,0,0)))
print('a\n',a)
print(type(a))
sc=scipy.sparse.csr_matrix(a)
print('a in compressed form\n',sc)
print(type(sc))
b=sc.toarray()
print('b\n',b)
print(type(b))
c=numpy.matrix(b)
print('c\n',c)
print(type(c))
