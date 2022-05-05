#!/usr/bin/python
def max_brackets(s):
    l = len(s)
    dp = [0]*l
    if not s:
        return 0

    for i in range(l):
        if s[i] == ')':
            if i-dp[i-1]-1 >=0 and s[i-dp[i-1]-1] == '(':
                dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]

    return max(dp)

case = [
    "(()",
    ")()())",
    "()",
    "((())))",
    "()(())",
    "()(()",
    "(()))())("
    ""
        ]
for i in case:
    print i,max_brackets(i)
