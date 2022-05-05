#!/usr/bin/python
def convert(columnTitle):
    res = 0
    for i in columnTitle:
        v = ord(i) - ord('A') + 1
        res = res*26 + v

    return res

case = [
        "A",
        "AA",
        "AB",
        "ZY"
        ]

for i in case:
    print i,convert(i)
