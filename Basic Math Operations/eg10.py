import numpy
a=numpy.matrix(((10,20),(30,40)))
print('a\n',a)
b=a+10
print('a+10\n',b)
b=a.__add__(10)
print('a.__add__(10)\n',b)
b=numpy.add(a,10)
print('numpy.add(a,10)\n',b)
a=numpy.matrix(((10,20),(30,40)))
print('a\n',a)
b=a-10
print('a-10\n',b)
b=numpy.subtract(a,10)
print('numpy.subtract(a,10)\n',b)
a=numpy.matrix(((10,20),(30,40)))
print('a\n',a)
b=a*10
print('a*10\n',b)
b=numpy.dot(a,10)
print('numpy.dot(a,10)\n',b)
a=numpy.matrix(((10,20),(30,40)))
print('a\n',a)
b=a/10
print('a/10\n',b)
b=numpy.divide(a,10)
print('numpy.divide(a,10)\n',b)
a=numpy.matrix(((12,24),(36,49)))
print('a\n',a)
b=a%10
print('a%10\n',b)
b=numpy.mod(a,10)
print('numpy.mod(a,10)\n',b)