import numpy
'''
set of equations are
2x+5y=20
3x+10y=35
x=5
y=2
'''
a=numpy.matrix(((2,5),(3,10)))
b=numpy.matrix(((20,),(35,)))
c=numpy.linalg.inv(a)
d=c*b
print('a\n',a)
print('b\n',b)
print('Inverse of a\n',c)
print('d\n',d)