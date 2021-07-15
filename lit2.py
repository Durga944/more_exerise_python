s = input("enter any string--->")
i=0
new=[]
c=0
while i<len(s):
    if s[i] not in new:
        new.append(s[i])
        c=c+1
        new.append(c)
    i=i+1
# print(new)
print(c)
