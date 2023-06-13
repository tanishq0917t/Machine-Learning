import numpy
a=numpy.matrix(((10,20),(30,40)))
b=a*a
print('a\n',a)
print('a^2\n',b)
b=numpy.square(a)
print('numpy.square(a)\n',b)     #This is squaring each term of matrix, not actually calculating a*a
b=numpy.power(a,2)
print('numpy.power(a,2)\n',b)     #This is squaring each term of matrix, not actually calculating a*a
b=numpy.power(a,3)
print('numpy.power(a,3)\n',b)
b=numpy.dot(a,a)
print('numpy.dot(a,a)\n',b)
