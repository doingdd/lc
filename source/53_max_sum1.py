#!/usr/bin/python
def max_sub(nums):
    _sum = nums[0]
    _sub_sum = nums[0]
    l = len(nums)
    for i in range(1,l):
        _sub_sum = max(nums[i],_sub_sum+nums[i])
        _sum = max(_sum,_sub_sum)

    return _sum



case = ([-2,1,-3,4,-1,2,1,-5,4],
        [1],
        [0],
        [-1,-1,-1]
        )
for i in case:
    print i,max_sub(i)
