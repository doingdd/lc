#!/usr/bin/python

def max_sub(A,B):
    num = 0
    l1 = len(A)
    l2 = len(B)
    dp = [[0]*(l2+1) for i in range(l1+1)]
    for i in range(1,l1+1):
        for j in range(1,l2+1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                num = max(num,dp[i][j])
            else:
                dp[i][j] = dp[i-1][j-1]
                #dp[i][j] = max(dp[i][j-1],dp[i-1][j])

    #print dp
    return num


case = [([1,2,3,2,1],[3,2,1,4,7]),
        ([1,2,3,2,1],[2,1,3,2,1]),
        ([1,2,3,2,1],[4,2,1,3,2,1,2,3,2,1]),
        ([1,2,3],[3,2,1]),
        ([1,2,3],[1,2,3])
        ]
for i in case:
    print i,max_sub(*i)

