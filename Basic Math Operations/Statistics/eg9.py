import numpy
import collections
import statistics
a=[100,200,300,100,200,300,400,500,300,700,800,900,1000,800]
b=numpy.sort(a)
print("Out Data Set:",b)
c=collections.Counter(b)
print('Frequency Count:',c)
d,e=(list(c.keys()),list(c.values()))
print("Data Unique Set(A):",d)
print("Frequency Set(B):",e)
f=numpy.cumsum(e)
print("Cummulative Sum(C):",f)
g=f[len(f)-1]
print('Last element of cummulative sum of frequencies:',g)
gc=g/2
print('Center of last element of cummulative sum of frequencies:',gc)
print(statistics.median_grouped(a))