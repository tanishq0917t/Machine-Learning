import numpy
a=numpy.matrix(((10,20,30,40),(50,60,70,80),(90,100,110,120),(130,140,150,160)))
print('a\n',a)
b=a.flatten('C')
print('b\n',b)
c=a.flatten('F')
print('c\n',c)
