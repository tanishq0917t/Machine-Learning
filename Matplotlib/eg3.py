import matplotlib.pyplot
import numpy
a=numpy.random.randint(50,size=10)
b=numpy.random.randint(100,size=15)
print(a)
print(b)
matplotlib.pyplot.plot(a)
matplotlib.pyplot.plot(b)
matplotlib.pyplot.show()