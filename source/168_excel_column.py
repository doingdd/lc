#!/usr/bin/python
def convert(columnNumber):
    def i2a(i):
        return chr(i+64) if i < 26 else None

    res = ''
    
    while columnNumber > 0:
        columnNumber -= 1
        res = chr(columnNumber%26 + 65) + res
        columnNumber /= 26

    return res



case = [
        1,28,701,2147483647,

        ]

for i in case:
    print i,convert(i)
