# def sort(l):
#     for i in range(len(l)):
#         min = i
#         for j in range(i,len(l)):
#
#             if (l[j] > l[min]):
#                 # (l[i] , l[i+1]) = (l[i+1] , l[i])
#                 min = i
#     # print(l)
#         (l[i],l[min]) = (l[min],l[i])
#         print(l)
# lst = [ 5, 1, 2, 8, 3, 4, 7, 9]
# sort(lst)

# def sort(list):
#     em_list = []
#     for i in range(len(list)):
#         if list[i] < list[i+1]:
#             em_list.append(list[i])
#     print(em_list)
lst = [ 5, 1, 2, 8, 3, 4, 7, 9]
# sort(lst)
lst.sort()
lst.pop(1)
lst.pop()
print(lst)