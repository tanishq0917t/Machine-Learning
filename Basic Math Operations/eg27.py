import numpy
a=numpy.matrix(((10,20,30,40),(50,60,70,80),(90,100,110,120)))
b=numpy.linalg.matrix_rank(a)
print('a\n',a)
print('Rank of A:',b)
b=numpy.trace(a)
print('Trace of A:',b)