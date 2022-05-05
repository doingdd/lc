#!/usr/bin/python
case = [
  ["sea","eat"],
  ["delete","leet"],
  ["a",""],
  ["a","b"]
]

def min_del_sum(s1, s2):
    """
    :type s1: str
    :type s2: str
    :rtype: int
    """
    m,n = len(s1),len(s2)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
            else:
                dp[i][j] = max(dp[i][j-1],dp[i-1][j])
    total = sum([ord(i) for i in s1+s2])

    return total - 2 * dp[m][n]


for i in case:
    print "case is {0}, result is {1}".format(i,min_del_sum(*i))
