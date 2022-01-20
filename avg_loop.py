from re import I


print("HELLO THIS IS THE CODE OF TAKING AVERAGE OF 5 No.")

# sum=0
# for i in range(0,5):
#     inp = int(input("ENTER THE NO. "))
#     sum += inp
# avg = sum/5
# print(avg) 

sum = 0
n = int(input())
for i in range(0,n+1):
    sum += i
print(sum/n)