import numpy
a=numpy.matrix(((1,2,3),(4,5,6),(7,8,9)))
print('a\n',a)
b=a.copy()
print('b\n',b)
c=a.view()
print('c\n',c)
c[0,0]=10
print('a\n',a)
print('c\n',c)
#View function is also working as 'b=a' then why view() exists? There is a difference between b=a and b=a.view()