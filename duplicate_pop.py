list = [0,2,2,2,4,5,9]
def remdup(l):
    li = []
    for i in l:
        if i not in li:
            li.append(i)
    print(li)
    return li

remdup(list)


