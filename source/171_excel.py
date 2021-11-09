#!/usr/bin/python
def excel(s):
    num = 0
    for i in s:
        v = ord(i) - ord('A') + 1
        num = num*26 + v

    return num

case = [('A',1),('AB',28),('ZY',701)]
for i in case:
    print i,excel(i[0]),i[1]
