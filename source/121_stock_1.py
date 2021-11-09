#!/usr/bin/python
def stock(nums):
    if not nums:
        return 0
    min_price = nums[0]
    max_profit = 0
    for i in nums:
        max_profit = max(i-min_price,max_profit)
        min_price = min(min_price,i)

    return max_profit


nums = [7,1,5,3,6,4]
print nums,stock(nums)

nums = [7,6,4,3,1]
print nums,stock(nums)

nums = [0,1]
print nums,stock(nums)

nums = [1]
print nums,stock(nums)

nums = []
print nums,stock(nums)

nums = [5,5,5,5]
print nums,stock(nums)
