import numpy
a=numpy.matrix(((1,2,3),(4,5,6),(7,8,9)))
print('a\n',a)
b=a
print('b\n',b)
b[0,0]=10
print('a\n',a)
print('b\n',b)
#Proof of pointer concept that a&b are just pointers pointing to numpy.matrix type object