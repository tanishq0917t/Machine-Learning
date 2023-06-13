import numpy
a=numpy.matrix(((10,20),(30,50)))
b=numpy.matrix(((1,2,5),(3,4,6)))
print(f"Shape of A matrix is {a.shape}")
print('a\n',a)
print(f"Shape of B matrix is {b.shape}")
print('b\n',b)
c=numpy.add(a,b)     #This will give error due to different shape of Matrix A & B
print(c)
