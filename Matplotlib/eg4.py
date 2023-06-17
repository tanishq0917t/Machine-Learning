import matplotlib.pyplot
import numpy
a=numpy.random.randint(50,size=10)
# b=numpy.random.randint(100,size=15) #due to this error will be there are dimension of a and b are not same
b=numpy.random.randint(100,size=10)
print(a)
print(b)
matplotlib.pyplot.plot(a,b)
matplotlib.pyplot.show()