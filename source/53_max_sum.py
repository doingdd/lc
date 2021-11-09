#!/usr/bin/python
## important: max(nums[i], nums[i] + _sum)

def get_max(nums):
    if not nums:
        return 0

    _sum = _max = nums[0]
    for i in range(1,len(nums)):
        _sum = max(nums[i],nums[i] + _sum)
        _max = max(_max,_sum)

    return _max


nums = [-2,1,-3,4,-1,2,1,-5,4]
print nums,get_max(nums)
nums = [1,1,1]
print nums,get_max(nums)
nums = [1]
print nums,get_max(nums)
nums = []
print nums,get_max(nums)
nums = [2,-1,3]
print nums,get_max(nums)
