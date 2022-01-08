#!/usr/bin/python

def sub_str(s1,s2):
    m,n = len(s1),len(s2)
    dp = [ [0]*(n+1) for _ in range(m+1) ]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    return dp[m][n]



a = [("abc","abc"),
     ("abcdef","ace"),
     ('','ace'),
     ('abc',''),
     ('aaa','a'),
     ('aaa','aaa'),
     ('abcdefedcba','bacdfecg'),
     ('abc','edf'),
     ('leetcode','etco')
     ]

for i in a:
    print i,sub_str(*i)
