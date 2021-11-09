#!/usr/bin/python

def get_max(nums):
    if not nums:
        return 0
    max_sum = tmp_sum = nums[0]
    n = len(nums)
    for i in range(1,n):
        tmp_sum = max(nums[i], tmp_sum +nums[i])
        max_sum = max(tmp_sum,max_sum)

    return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]
print nums,get_max(nums)
nums = [1,1,1]
print nums,get_max(nums)
nums = [1]
print nums,get_max(nums)
nums = []
print nums,get_max(nums)
