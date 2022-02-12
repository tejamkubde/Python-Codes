def sumsquare(l):
    odd_li = []
    even_li = []
    sum_odd = 0
    sum_even = 0
    def odd(l):
        for i in l:
            if i%2 != 0:
                odd_li.append(i)

    odd(l)
    for a in odd_li:
        sum_odd += a*a

    def even(l):
        for i in l:
            if i%2 == 0:
                even_li.append(i)

    even(l)
    for a in even_li:
        sum_even += a*a

    final_li = [sum_odd,sum_even]
    print(final_li)

sumsquare([1,3,5])
