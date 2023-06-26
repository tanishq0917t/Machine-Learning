import matplotlib.pyplot
import numpy
def myFunc(a):
    return a[1]

a=numpy.array([[2,3],[1,2],[1,4],[2,4],[1,3],[3,2],[3.5,1],[1,3.5],[0.5,1.5]])
b=numpy.array([[6,3],[5,2],[4,4],[3.5,4.5],[5,4],[6,3],[5,3]])
n=int((len(a)+len(b))**0.5)
if n%2==0: n+=1
x,y=a.T
c=(4,3.5)
matplotlib.pyplot.scatter(x,y,color='r')
x,y=b.T
matplotlib.pyplot.scatter(x,y,color='g')

frequencyList=[]
for i in a: frequencyList.append(('A',((c[0]-i[0])**2+(c[1]-i[1])**2)**0.5,i[0],i[1]))
for i in b: frequencyList.append(('B',((c[0]-i[0])**2+(c[1]-i[1])**2)**0.5,i[0],i[1]))

frequencyList.sort(key=myFunc)
frequencyList=frequencyList[:n]
print(frequencyList)
ans=None
aa=0
bb=0
for i in frequencyList:
    if i[0]=='A':
        aa+=1
        matplotlib.pyplot.plot([c[0],i[2]],[c[1],i[3]],'ro-')
    if i[0]=='B':
        bb+=1
        matplotlib.pyplot.plot([c[0],i[2]],[c[1],i[3]],'go-')
    if aa>bb: ans='Red'
    else: ans='Green'
matplotlib.pyplot.plot(c[0],c[1],'ko')
matplotlib.pyplot.title(f"KNN Algorithm, Query Point ({c[0]},{c[1]}) belongs to {ans} group")
matplotlib.pyplot.show()
