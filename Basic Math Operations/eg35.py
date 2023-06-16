import numpy
a=numpy.matrix(((1,2,3),(4,5,6),(7,8,9)))
print('a\n',a)
b=a.copy()
print('b\n',b)
b[0,0]=10
print('a\n',a)
print('b\n',b)
#Creating a shallow copy of "a" matrix as "b", then changing element in "b" which is not reflected in "a" matrix