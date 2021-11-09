#!/usr/bin/python
def reverse(s):
    word = ''
    stack = []
    r_s = ''
    for i in s:
        if i != ' ':
            word += i
        elif i == ' ' and word:
            stack.append(word)
            word = ''

    if word:
        stack.append(word)

    while stack:
        if r_s:
            r_s += (' ' + stack.pop())
        else:
            r_s += stack.pop()

    return r_s

case = ["the sky is blue",
        "  hello world",
        "a good    example",
        "  Bob    Loves  Alice   "
        ]

for i in case:
    print i,'reversed:  ',reverse(i)
