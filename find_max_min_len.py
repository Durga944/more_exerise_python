list=[[0],[1,3],[5,7],[9,11],[13,15,17]] # edge case
i=0
c=0
a=[]
b=[]
while i<len(list):
    d=len(list[i])
    a.append(list[i])
    b.append(d)
    c=c+1
    i=i+1
# print(a)
# print(b)
j=0
data={}
c=[]
while j<len(a):
    v=b[j]
    data[v]=a[j]
    j=j+1
# print(data)
# print(type(data))
k=0
max=0
while k<len(b):
    if b[k]>max:
        max=b[k]
    k=k+1
# print(max)
x=data[max]
# print(x)
xyz=(max,x)
print(xyz)
m=0
min=b[m]
while m<len(b):
    if b[m]<min:
        min=b[m]
    m=m+1
# print(min)
y=data[min]
abc=(min,y)
print(abc)
    





    


    




