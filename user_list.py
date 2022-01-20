# CREATING LIST BY TAKING INPUT FROM THE USER :)

a = []
leng = int(input("enter the length of the list: "))
for i in range(leng):
    inp = int(input("enter the nos: "))
    a.append(inp)
print(a)
print(type(a))