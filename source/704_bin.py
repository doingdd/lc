#!/usr/bin/python
def bin_search(nums,target):
    left,right = 0,len(nums) - 1
    while left <= right:
        mid = left + (right-left)/2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1

    return -1
            



nums = [-1,0,3,5,9,12]
target = 9
print nums,target,bin_search(nums,target)
nums = [1,2,3]
target = 0
print nums,target,bin_search(nums,target)

nums = [1,2,3]
target = 4
print nums,target,bin_search(nums,target)

nums = [1]
target = 9
print nums,target,bin_search(nums,target)

nums = [12]
target = 12
print nums,target,bin_search(nums,target)

nums = []
target = 9
print nums,target,bin_search(nums,target)
