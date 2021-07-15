name=["pravi","durga","pihu","kuhu","monu"]
i=0
while i<len(name):
    if type(name[i])==str:
        b=name[i].replace("m","s")
        name[i]=b
    i=i+1
print(name)