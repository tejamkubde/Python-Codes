def gcd(m,n):
    abc = str(m)
    bcd = str(n)
    great = 0
    for i in range(1,16):
        if m%i==0 and n%i==0:
            great =str(i)
    print("Greatest Common Divisor of " + abc + " and " + bcd + " is " +great)


a = int(input("enter 1st no:- "))
b = int(input("enter 2nd no:- "))
gcd(a,b)
