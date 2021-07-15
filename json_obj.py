# json_object = {"user":[{"username":"durga","password":"durga18@"},{"username":"pravi","password":"pravi19@"}]}
# var=json_object["user"]
# print(len(var))
# index=0
# user1=input("enter any name")
# while index<len(var):
#     if var[index]["username"]==user1:
#         print("yes")
#         # break
#     else:
#             print("no")
#         # break
#     index=index+1


dic = {"user":[{"username":"durga","password":"durga18@"},{"username":"pravi","password":"pravi19@"}]}
var=dic["user"]
print(len(var))
index=0
user1=input("enter any name")
while index<len(var):
    if var[index]["username"]==user1:
        print("yes")
    else:
        print("no")
    index=index+1
