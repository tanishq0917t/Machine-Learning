import statistics
import numpy
a=[10,2,40,35]
print('Data Set:',a)
b=statistics.mean(a)
print('Mean of Data Set:',b)
c=numpy.subtract(a,b)
print('Difference of Data Set and Mean:',c)
d=numpy.square(c)
print('Squared Difference:',d)
e=statistics.mean(d)
print('Variance: (mean of squared difference):',e)
f=statistics.pvariance(a)
print('Variance:',f)
g=numpy.sqrt(e)
print("SQRT of variance:",g)
h=statistics.pstdev(a)
print("STD DEV:",h)