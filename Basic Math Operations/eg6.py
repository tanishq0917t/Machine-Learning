import numpy
a=numpy.matrix(((1,2),(3,4)))
#print(a)
#print(type(a))
b=numpy.matrix(((5,6),(7,8)))
print('a\n',a)
print('b\n',b)
c=a+b
print('a+b\n',c)
c=a.__add__(b)
print('a.__add__(b)\n',c)
c=numpy.add(a,b)
print('numpy.add(a,b)\n',c)
d=b-a
print('b-a\n',d)
