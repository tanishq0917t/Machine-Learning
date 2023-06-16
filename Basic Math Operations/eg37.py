import numpy
a=numpy.matrix(((1,2,3),(4,5,6),(7,8,9)))
b=a
c=a.copy()
d=a.view()
print("Id of a:",id(a))
print("Id of b:",id(b))
print("Id of c:",id(c))
print("Id of d:",id(d))
#Id of "a" and "d" are different so why changes in "d" are reflecting in "a" also?
#This is because when a copy is made by view() function then that object is little different from normal object
#This view()'s object will make changes in orignal object also.