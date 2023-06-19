import matplotlib.pyplot
import numpy
a=numpy.random.randint(100,size=50)
b=numpy.random.randint(100,200,size=50)
matplotlib.pyplot.scatter(a,b)
matplotlib.pyplot.show()