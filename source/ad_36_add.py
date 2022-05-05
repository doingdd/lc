#!/usr/bin/python


def toInt(x):
    y = 0
    c = 0
    for i,v in enumerate(x[::-1]):
        if v.isdigit():
            y += (36**i * int(v))
        else:
            y += (36**i *(ord(v) - ord('a') + 10))

    return y

def toChar(x):
    y = ''
    while (x / 36) >= 0:
        if x == 0 and x%36 == 0:
            break

        v = str(x%36) if (x%36)<10 else chr(x%36 - 10 + ord('a')) 
        y = v + y
        x /= 36

    return y

def add36(a,b):
    '''
        type a,b: str
        type res: str
    '''

    i,j = len(a)-1 ,len(b) -1 
    c = 0
    res = ''
    while i>=0 or j >=0:
        x = toInt(a[i]) if i >=0 else 0
        y = toInt(b[j]) if j >=0 else 0
        v = toChar((x + y + c) % 36)
        c = (x+y+c)/36
        res = v + res
        i -= 1
        j -= 1

    if c:
        res = str(c) + res
    return res

case = [
    ["1b","2x"],
    ["12","24"],
    ["1","1"],
    ["0","1"],
    ["zz","aa"]
]
for i in case:
    a = toInt(i[0])
    b = toInt(i[1])

    print i,a,b,
    print add36(*i),toInt(add36(*i))
