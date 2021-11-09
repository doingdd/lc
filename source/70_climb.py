#!/usr/bin/python
def climb(n):
    if n <= 2:
        return n
    a,b = 1,2
    for i in range(3,n+1):
        a,b = b, a+b

    return b


n = [2,1,0,3,4,5,6]
for i in n:
    print i,climb(i)

