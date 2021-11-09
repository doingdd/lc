#!/usr/bin/python

def rm(num,k):
    stack = []
    if len(num) < 2:
        return '0'

    for i in num:
        while k > 0 and stack and stack[-1] > i:
            stack.pop()
            k -= 1

        stack.append(i)
    while k > 0:
        stack.pop()
        k -= 1

    return ''.join(stack).lstrip('0') or '0'





case = [('1432219',3),
        ('10200',1),
        ('10',2),
        ('10200',2)
        ]
for i in case:
    print i,rm(*i)
