#!/usr/bin/python

case = [
  [123,321],
  [-123,-321],
  [120,21],
  [0,0],
  [-2147483648,0],
  [2147483647,0],
  [111,111],
  [-331122,-221133]
]

def reverse(x):
    y = 0
    right = 2**31 - 1 
    flag = 1 if x > 0 else -1
    x = abs(x)
    while x:
        n = x % 10
        if y > right/10:
            return 0
        if y == right/10 and n > right%10:
            return 0
        
        y = y*10 + n
        x /= 10

    return flag * y

for i in case:
    print "case is {0},result is {1}".format(i[0],reverse(i[0]))
