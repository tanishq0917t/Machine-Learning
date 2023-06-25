import matplotlib.pyplot
import numpy
a=[10,20,30,40,50,56,5]
b=[40,30,3,40,5,30,4]
c,=matplotlib.pyplot.plot(a)
d,=matplotlib.pyplot.plot(b)
print(c)
print(type(c))
c.set_color('r')
d.set_color('#000000')
matplotlib.pyplot.show()
