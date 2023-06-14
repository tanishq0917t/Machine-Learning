import numpy
#Create csv file
a=numpy.matrix(((10,20),(30,40)))
numpy.savetxt("whatever",a,delimiter=',')