#output[2,3,3,-1,-1,6,7,-1,8]
list =[2,3,8,0,0,6,7,0,3]
i=0
while i<len(list):
    if list[i]==0:
        list[i]=-1
    i+=1
print(list)
list.sort()
print(list)



        
        
        
        
        
        