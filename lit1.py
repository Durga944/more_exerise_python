# logical_question
num=[2,7,11,15]
target=int(input("enter any num"))
index=0
new=[]
while index<len(num):
    sum=0
    while sum<len(num):
        var=num[sum]+num[index]
        if var==target:
            new.append(index)
        sum=sum+1
    index=index+1
print(new)


    