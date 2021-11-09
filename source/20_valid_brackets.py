#!/usr/bin/python

def valid(s):
    pair = {')':'(',
            ']':'[',
            '}':'{'
            }
    stack = []
    for ch in s:
        if ch in pair:
            if not stack or stack[-1] != pair[ch]:
                return False

            stack.pop()
        else:
            stack.append(ch)


    return True if not stack else False


case = ["()",'()[]{}','(]','([)]','{[]}']
for i in case:
    print i,valid(i)

