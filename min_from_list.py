def minim(list):
    minimum = 10000
    for i in list:
        if(minimum > i):
            minimum = i
    print(minimum)
    
list = [20,50,1000,10,50,60,88,65,123]
minim(list)
# list.sort()
# print(list[0])

list1 = [20,50,1000,150,60,88,65,123]
minim(list1)