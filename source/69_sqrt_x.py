case = [
  4,8,3,0,10,9,81
]
def sqr(x):
    l,r,ans = 0,x,-1
    while l <= r:
        mid = (l+r)//2
        if mid*mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans

for i in case:
    print(i)
    print(sqr(i))

