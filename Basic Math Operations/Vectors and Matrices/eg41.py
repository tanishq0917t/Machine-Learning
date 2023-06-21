import numpy
def get_max(a):
    max=a[0]
    for i in range(1,len(a)):
        if a[i]>max: max=a[i]
    return max

a=numpy.random.randint(100,size=(5,4))
print('a\n',a)
print(type(a))
c=numpy.apply_along_axis(get_max,1,a)
print('c\n',c)
d=numpy.apply_along_axis(get_max,0,a)
print('d\n',d)