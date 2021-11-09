#!/usr/bin/python

def cal(s):
    pre = '+'
    stack = []
    num = 0 
    if not s:
        return

    for i,v in enumerate(s):
        if v == ' ':
            continue

        #print i
        if v.isdigit():
            num = num*10 + int(v)
            #print num

        if i == len(s) - 1 or v in '+-*/':
            if pre == '+':
                stack.append(num)
            elif pre == '-':
                stack.append(-num)
            elif pre == '*':
                stack[-1] = stack[-1]*num
            elif pre == '/':
                stack[-1] = stack[-1]/num

            pre = v
            num = 0

    #print stack
    return sum(stack)

case = [' 1 + 2 *3',
        '',
        '1+2+3',
        '2-3/2',
        '3+1 * 5 /2/2',
        '10+21*2']
for i in case:
    print i,cal(i)
    #break
