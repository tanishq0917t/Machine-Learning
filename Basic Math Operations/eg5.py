import numpy
coefficient=[2,3,4,5,10]
poly=numpy.poly1d(coefficient)
print(type(poly))
print(poly)
x=2
result=poly(2)
print(result)
