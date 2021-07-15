import json
file=open("emoji.json")
data=json.load(file)
# print(d)
title=input("enter title =")

for i in data:
    # print(i)
    for j in i:
        # print(j)
        if title==i[j]:
            print(i["symbol"])
            print(i["keywords"])

