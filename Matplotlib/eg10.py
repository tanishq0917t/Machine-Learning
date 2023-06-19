import matplotlib.pyplot
a=[10,20,30,40]
b=[80,160,200,500]
matplotlib.pyplot.plot(a,b,linestyle=':',marker='x',color='r')
matplotlib.pyplot.savefig("image.png")
matplotlib.pyplot.show()
