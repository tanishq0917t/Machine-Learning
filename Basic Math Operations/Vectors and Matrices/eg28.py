import numpy
a=numpy.matrix(((10,20,30,40),(50,60,70,80),(90,100,110,120),(130,140,150,160)))
b=numpy.linalg.matrix_power(a,2)
print('a^2\n',b)
c=a*a
print('a*a\n',b)
b=numpy.linalg.matrix_power(a,3)
print('a^3\n',b)
c=a*a*a
print('a*a*a\n',b)