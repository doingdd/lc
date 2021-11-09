#!/usr/bin/python

def f(n):
    if n < 2:
        return n

    return f(n-2) + f(n-1)

def f1(n):
    if n < 2:
        return n

    a,b = 0,1
    for i in range(n-1):
        a,b = b,a+b

    return b
        

print f1(1)
print f1(2)
print f1(3)
print f1(4)
print f1(5)
