import numpy
a=numpy.matrix(((3,100,10,500000),(4,20,20,400000),
                (5,40,15,750000),(4,140,5,850000),
                (5,40,15,700000),(6,10,15,650000),
                (2,20,15,450000)))
# print("Before Mean Normaliztion\n",a)

def myFunc(a):
    mean=numpy.mean(a)
    min=numpy.min(a)
    max=numpy.max(a)
    print()
    print("Array:",a)
    print("Mean:",mean)
    print()
    x=[(i-mean)/(max-min) for i in a]
    return x

aa=numpy.apply_along_axis(myFunc,axis=0,arr=a)
# print()
# print(aa)