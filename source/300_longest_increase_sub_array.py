#!/usr/bin/python

case = [
  [10,9,2,5,3,7,101,18],
  [10,9,2,5,3,7,101,18],[7,7,7,7,7,7,7],
  [],
  [1],
  [3,2,1],
  [1,1,0,0],
  [1,2,3,4,5]
]
def lenOFLIS(nums):
    n = len(nums)
    if not n:
        return 0

    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i],dp[j] + 1)

    return max(dp)

for i in case:
    print "case is {0},result is {1}".format(i,lenOFLIS(i))
