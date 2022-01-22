def counter(list):
        count = 0
        for i in list:
            count += 1
        print(count)

list = [10,20,1000,50,60,88,65,123]
counter(list)

list1 = [10,20,1000,50,60,88,65,123,"number",1010,5015210]
counter(list1)

list2 = ["ketan",1876,1554,45622,1254,54687,5456,10,20,1000,50,60,88,65,123]
counter(list2)


# Function with a function

# def details():
#     def function(detail):
#         for i in detail.keys():
#             print(detail[i])
#     detail  = {"name":"tejam","surname":"kubde","roll_no":19}
#     function(detail)
    
# details()