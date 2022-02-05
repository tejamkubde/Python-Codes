# import numpy as np
# a = np.array([1,2,3,4,5],ndmin = 2)
# print(a)

# def nprint(message,n):
#     while(n>0):
#         print(message)
#     n-=1
# nprint('z',5)

# a ={1:2, 'list':[1,2],3:5}
# b = {4:5,3:7}
# a.update(b)
# print(a)

# days = ['sun','mon','tue','wed','thu','fri','sat']
# print(days[-5:-2])

# thisdict = {
#    " college":'abc',"sec":'a',"DOB":2022
# }
# print(thisdict[" college"])

# print(list(range(0,8,2)))
import numpy
import numpy as np
# arr = [2.33,5.344,9.66,5.11]
# floor_arr = np.floor(arr)
# print(floor_arr)

# tuple = (1,2,3,4)
# tuple.appen
# a = np.arange(5)
# a[[1,3,4]] = 0
# print(a)

# arr = np.array([1,5,7,4,8,2,4,1,8,9])
# arr = arr*2
# print(arr[2:6])

# a = np.array([[1,2,3],[0,1,4]])
# b = np.zeros((2,3), dtype=np.int16)
# c = np.ones((2,3), dtype=np.int16)
# d = a+b+c
# print(d[1,2])

a = np.array([[1,2,7],[3,4,8]])
# print(arr[1,0:4])
np.std(a)
ss=np.std(a,axis=0)
rr = np.std(a,axis=1)
print(ss,rr)