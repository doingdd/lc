#!/usr/bin/python
from __future__ import division

def cal(s):
    pre = '+'
    stack = []
    n = len(s)
    num = 0
    for i,v in enumerate(s):
        if v.isdigit():
            num = num * 10 + int(v)

        if i == (n-1) or v in '+-*/':
            if pre == '+':
                stack.append(num)
            elif pre == '-':
                stack.append(-num)
            elif pre == '*':
                stack.append(num*stack.pop())
            elif pre == '/':
                stack.append(int(stack.pop()/num))
            num = 0
            pre = v

    #print stack
    return sum(stack)



case = ["2+3*2",
       " 2 + 3 * 2 ",
       " 2 + 3/2",
       "2*30+1",
       "2-3/2"
       ]

for i in case:
    print i,cal(i)
