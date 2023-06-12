import numpy
a=numpy.array([10,20,30])
b=numpy.array([5,6,7])
c=numpy.dot(a,b)
print('a.b',c)
d=a@b
print('a.b via a@b',d)
