#!/usr/bin/python
import re

def myAtoi(s):
    num = 0
    flag = 1

    for i in s:
        if i == ' ':
            continue
        if i == '-':
            flag = -1
            continue

        if num and not i.isdigit():
            return num
        else:
            i = int(i)
            if (num*10+i)*flag > 2**31-1:
                num = 2**31-1
                return num

            if (num*10+i)*flag < -2**31:
                num = -2**31
                return num
            num = num*10 + i

    return num
def myAtoi2(s):
    r = re.match(' *([+-]?\d+)',s)
    if not r:
        return 0
    num = int(r.group(1))
    #print num
    return min(max(num,-2**31),2**31-1)



case = [ 
    "42",
    "-32",
    "  32",
    "  -32",
    "123 wor",
    "  -12312 sdfs",
    "2147483648",
    "  -2147483648",
    "  - ",
    "123- wor",
    " 0"
        ]

for i in case:
    #print i,myAtoi(i)
    print i,myAtoi2(i)
