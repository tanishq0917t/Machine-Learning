import numpy
a=numpy.matrix(((10,20,30,40),(50,60,70,80),(90,100,110,120),(130,140,150,160)))
b,c=numpy.linalg.eig(a)
print('Eigen values:\n',b)
print('Eigen vectors:\n',c)