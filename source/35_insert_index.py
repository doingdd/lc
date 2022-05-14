#!/usr/bin/python
case = [
	([1,3,5,6],2),
  ([1,3,5,6],5),
  ([1,3,5,6],7)
]

def insert_index(nums,target):
    l = len(nums)
    left,right = 0,l
    while left < right:
        mid = left + (right-left)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid
    return left

for i in case:
    print i,insert_index(*i)
