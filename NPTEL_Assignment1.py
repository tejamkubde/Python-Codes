# def f(x):
#     d=0
#     while x >= 1:
#         (x,d) = (x/7,d+1)
#     return(d)
#
# print(f(3456))

def h(n):
    s = 0
    for i in range(2,n):
        if n%i == 0:
           s = s+i
    return(s)

print(h(60)-h(45))

# def g(m,n):
#     res = 0
#     while m >= n:
#         (res,m) = (res+1,m/n)
#     return(res)
#
# print(g(375,4))

# def mys(m):
#   if m == 1:
#     return(1)
#   else:
#     return(m+mys(m-1))
#
# print(mys(4))