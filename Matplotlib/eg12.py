import matplotlib.pyplot
import numpy
a=(10,15,25,50)
captions=("Pizza","Burger","Pasta","Chips")
#matplotlib.pyplot.pie(a,labels=captions)
matplotlib.pyplot.pie(a,labels=captions,explode=(.1,.1,.1,.4))
matplotlib.pyplot.show()