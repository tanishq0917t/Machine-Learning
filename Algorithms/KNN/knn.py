def myFunc(a):
    return a[1]
a=[(2,3),(1,2),(1,4),(2,4),(1,3),(3,2),(3.5,1),(1,3.5),(0.5,1.5)]
b=[(6,3),(5,2),(4,4),(3.5,4.5),(5,4),(6,3),(5,3)]
n=int((len(a)+len(b))**0.5)
if n%2==0: n+=1
print("N for the following data sets is:",n)
c=(3.5,3.5)
print("Data Set (A):",a)
print("Data Set (B):",b)
print("Query Point (C):",c)
frequencyList=[]
for i in a: frequencyList.append(('A',((c[0]-i[0])**2+(c[1]-i[1])**2)**0.5))
for i in b: frequencyList.append(('B',((c[0]-i[0])**2+(c[1]-i[1])**2)**0.5))
frequencyList.sort(key=myFunc)
frequencyList=frequencyList[:n]
print(frequencyList)
ans=None
aa=0
bb=0
for i in frequencyList:
    if i[0]=='A':aa+=1
    if i[0]=='B':bb+=1
    if aa>bb: ans='A'
    else: ans='B'
print()
print(f"{c} belongs to {ans} group")
