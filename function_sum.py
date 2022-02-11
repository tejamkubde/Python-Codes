
def addition(list):
    sum = 0
    for i in list:
        sum += i 
    return(sum)

list = []    
iterates = int(input("No. of elements you want to enter: "))
for i in range(iterates):
    value = int(input("Enter the no: "))
    list.append(value) 

print(list)
user = int(input("GUESS THE RESULT:- "))
if user == addition(list):
    print("Hurray!! You won :)")
else:
    print("Sorry!! You Lost :(")