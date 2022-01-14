case = [
   [100,4,200,1,3,2],
   [0,3,7,2,5,8,4,6,0,1],
   [-1,0],
   [1,2,4,5,3],
   [-2,-3,-3,7,-3,0,5,0,-8,-4,-1,2],
   []
]

def longest(nums):
    n = 0
    dp = {}
    for i in nums:
        if i not in dp:
            left = dp.get(i-1,0) 
            right = dp.get(i+1,0) 
            now = left + right + 1
            n = max(n,now)
            dp[i] = now
            dp[i-left] = now
            dp[i+right] = now

    return n



for i in case:
    print(i)
    print (longest(i))
