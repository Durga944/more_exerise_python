#Dictionary
# <<<<<<<<<<<<<<<<<<<Dictionary is a unordered collection of item .Each item of a dictionary is represented in the 
# the form of key value pairs.creating a dictionary:placing items inside a curly braces.
# An item has a key uncorresponding value i.e express as a pair.>>>>>>>>>>>>>>>> 

#Example : -
# my_dic = {1:"apple",2:"banana",3:"cherry"}
# print(my_dic)
# for x in my_dic:
    # print(x)
    # print(my_dic[x])
# print(my_dic[1])

#for keys
# for x in my_dic:
#   print(x)

#for value
# for x in my_dic:
#   print(my_dic[x])

    # print(my_dic.get(x))

#for value_method
# for x in my_dic.values():
#   print(x)

#for keys_method
# for x in my_dic.keys():
#   print(x)

#items_method
#both keys and value
# for x, y in my_dic.items():
#   print(x, y)


#upatate_method
# dic = {"name":"durga","age":19}
# dic["age"]=20
# print(dic)

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)
# thisdict.update({"color": "red"})
# print(thisdict)


# thisdict = {
  # "brand": "Ford",
  # "electric": False,
  # "year": 1964,
  # "colors": ["red", "white", "blue"]
# }
# print(thisdict["colors"])


#pop()_method
# squre={1:2,2:3,3:4,5:6}
# print(squre.pop(5))
#clear_method
# squre.clear()
# print(squre)

my_list1=[1,2,3,4,5]
my_list2=["a","b","c","d","e"]
i=0
c={}
while i<len(my_list1):
  c[my_list1[i]]=[my_list2[i]]
  # c[my_list1[i]]=my_list2[i]
  i=i+1
print(c)





