# a=47
# b=5
# c=a//b
# d=a % b
# print(c*b+d)
#
# print(2+10/5-4)

# import matplotlib.pyplot as plt
# x=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# plt.plot(x,2*x)

# atuple=('a','b',5.7,9)
# z=list(atuple)
# print(z)

# aset={2,4,6,8,2,5,6}
# print(aset)
#
# xdict=dict([('k1','v1'), ('k2','v2'),('k3','v3')])
# print(xdict)

# xdict=dict([(1,'v1'), (2,'v2'),(3,'v3')])
# ydict=dict([('v1',1), ('v2',2),('v3',3)])
# ydict.update(xdict)
# ydict['v2']=23
# print(ydict)

# import re
# pattern='b.+d'
# s='dbhfj'
# print(re.search(pattern, s))
import exceptional as exceptional

try:
    z = 3+input('Input a number: ')
except exceptional as e:
    print(e)