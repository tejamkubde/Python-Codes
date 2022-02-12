def find(l):
    a = l
    to_find = int(input("Enter the key you want to find: "))
    for i in range(len(a)):
        if a[i] == to_find:
            print(i)

        else:
            continue

n = int(input("Enter the no. of elements you want in your list:- "))
lst = []
for i in range(n):
    abc = int(input("enter the no: "))
    lst.append(abc)
find(lst)