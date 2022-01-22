d = {"f_name":"Tejam","l_name":"Kubde","roll_no":19,"online":[True,False],1900560380:"enrollment_no",34:{"age":19}}
print(d)
# print(type(d)) #<class 'dict'>

# printing values using for loop
# for i in d.keys():
#     print(d[i])
    
# print(type(d.keys()))
# print(type(d.values()))

# print(d["f_name"])
# print(d[1900560380])

# what if we have 2 same keys but different value assigned to it
#   if replaces the 1st assigned value to the latest one 
# print(d["online"])

# print(type(d[34]))


# for accessing the values in the dict inside another dict
print(d[34]["age"])

# in dict there is no indexing as we can access the keys by using the key name and not by their indexes.

# for add new key and value pair:
# 1st way
# d["hobby"]="playing"
# print(d)

# 2nd way 
# d.update({"hobby":"cricket"})
# print(d)

# deleting any key in dict
# del d[34]
# print(d)

# deleting whole dict
# del d 
# print(d) #show an error because 1st we have deleted the dict and then we have printed it

# after deleting the dict its whole existence is removed
# suppose we have to empty the dict
d.clear()
print(d) #{}
