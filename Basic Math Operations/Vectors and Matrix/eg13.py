import numpy
a=numpy.matrix(((10,20),(30,40)))
b=numpy.linalg.inv(a)
print('a\n',a)
print('Inverse of a:\n',b)
