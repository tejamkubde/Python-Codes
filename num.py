import numpy as np

# arr = np.array([1, 2, 3])
# print(arr)
# print(type(arr))
# print(arr.shape)  # returns the type like 2-dimensional or 3-dimensional array
# print(arr[0], arr[1], arr[2])
"""
b = np.array([[1,2,3],[4,5,6],["abc","def","xyz"]])
print(b[0][1])
print(b.shape)

ab = np.zeros([4,4])
print(ab)

print()

ba = np.ones([4,4])
print(ba)

print()

abc = np.full([3,3] , 2003)
print(abc)

print()

cab = np.eye(3)  #identical matrix i.e the diagonal values are 1 and other values are 0
print(cab)

print()

bac = np.random.random((2,2)) #returns the random value but in 0. float manner
print(bac)

print()

aa = np.random.randint(2,100,(3,3))
print(aa)

print()
"""

# addition of 2 matrix
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

# sum = np.add(a,b)
sum = a + b
print(sum)

print()
# subtraction of 2 matrix
# sum = np.subtract(b,a)
sum = b-a
print(sum)

print()
# multiplication of 2 matrix
sum = np.multiply(a,b) #output is wrong as this do array multiplication and not matrix
print(sum)

print()
# for proper matrix multiplications
sum = np.dot(a,b)
print((sum))

print()
# squareroot
print(np.sqrt(a))