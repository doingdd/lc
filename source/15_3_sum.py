#!/usr/bin/python
def sum3(nums):
    res = []
    l = len(nums)
    if l < 3:
        return res

    nums.sort()
    for i in range(l):
        if nums[i] > 0:
            return res

        if i > 0 and nums[i] == nums[i-1]:
            continue

        j,k = i+1,l-1
        while j < k:
            result = nums[i] + nums[j] + nums[k]
            if result == 0:
                if [nums[i],nums[j],nums[k]] not in res:
                    res.append([nums[i],nums[j],nums[k]])
                k -= 1
                j += 1
            elif result > 0:
                k -= 1
            elif result < 0:
                j += 1

    return res

case = [
        [-1,0,1,2,-1,-4],
        [0],
        [],
        [-1,-1],
        [1],
        [1,2,3,-6],
        [1,-1],
        [-2,0,0,2,2]
        ]
for i in case:
    print i,sum3(i)
