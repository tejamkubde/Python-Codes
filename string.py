string = "This is an Example of the string"
print(string)
print(len(string))

# print(string[:])
# print(string[5:])
# print(string[:5])
# print(string[11:19])


# finding an character in the string using for loop
# for i in range(len(string)):
#     if string[i] == "E":
#         print(i)
        
# finding an character in the string using find method
char = "e"
# print(string.find(char))
# print(string.rfind(char)) #r is the reverse 

print(string.upper()) #upper case
print(string.lower()) #lower case
print(string.capitalize()) #just converts the first letter to upper case
print(string.split()) #split function splits the string on the basis of spaces and creates a list out of it.
# also in the split function we can specify the seperator in quotes in the split brackets
# string1 = "This#is#an#Example#of#the#string"
# print(string1.split("#"))

print(string.count("i")) #count function should have at least on argument and it counts the no. of specified letter in the string
print(string.zfill(40)) #zfill function just adds the no. of zeros in the beginning of the string if the string doesn't contain the specified length.