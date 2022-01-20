# list = ["tejam",True,90]
# print(list)
# print(type(list))

# list = ["tejam",True,["kubde",100],90]
# print(list[2])

# list = ["tejam",True,[list,"op","joddddddddd"],90]
# print(list[2])

# list = ["tejam",True,["kubde",100],90]
# print(list[2][0])


list = ["tejamm",True,["kubde",100],90]
# list[0]="TEJAM"
# print(list)


# VARIOUS COMMANDS IN LIST 
# 1. append: used to add an element at the last of the list
# list.append("tyjm")
# print(list)

# 2. insert: used to insert any element at a specified position
# list.insert(1,"kubde")
# print(list)

# 3. sort: used to sort the list from ascending to descending /* only applicable if the list has same datatype elements
# list.sort()
# print(list)

# 4. del: used to delete any element from a list
# del(list[1])
# print(list)

# 5. : =to select a range from a given list /* in this 1st idex is included and 2nd index is excluded
# print(list[1:3])

# 6. len: used to find the length of the given list 
# print(len(list))

# 7. min: used to find the minimum value in the list  
list1 = [10,20,50,1000,50,60,88,65,123]
# print(min(list1))

# 8. max: used to find the max value in the list  
list1 = [10,20,50,1000,50,60,88,65,123]
print(max(list1))

# 9. sum: used to find the sum of the elements in the list. 
# print(sum(list1))

# 10. using for loop in list :
    # 1. 
        # for i in list:
        #     print(i)
    
    # 2.
        # for i in range(len(list)):
        #     print(list[i])
        
list1 = [10,20,50,1000,50,60,88,65,123]
# for i in list1:
#     if i < list1:
#         print(i)


#  DIFF WAYS TO FIND LENGTH OF A LIST
# print(len(list1))

# count = 0
# for i in list1:
#     count += 1
# print(count)