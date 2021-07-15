# name = "my name is durga"
# output My Name Is Durga
# d=name.split()
# print(d)

# name = input("enter any num:-")
# print(type(name))
# d=name.split()
# print(d)

# name=input("enter any name:-")
# d=name.title()
# d=name.swapcase()
# print(d)

name=input("enter any name:-")
d=name.split()
str=" "
i=0
while i<len(d):
    j=0
    while j<len(d[i]):
        # print(j)
        if j==0:
            str=str+d[i][j].upper()
        else:
            str=str+d[i][j]
        j+=1
    str+=" "
    i+=1
print(str)
# print(type(str))

