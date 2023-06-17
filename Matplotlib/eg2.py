import matplotlib.pyplot
data=[]
for i in range(10):
    data.append(i**3)
matplotlib.pyplot.plot(data)
matplotlib.pyplot.show()