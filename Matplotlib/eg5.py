import matplotlib.pyplot
import numpy
a=numpy.random.randint(50,size=10)
b=numpy.random.randint(100,size=10)
print(a)
print(b)
c=[]
for i in a: c.append(i)
for i in b: c.append(i)
print(c)
matplotlib.pyplot.plot(c)
matplotlib.pyplot.show()