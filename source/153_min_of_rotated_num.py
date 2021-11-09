#!/usr/bin/python

def find_min(nums):
    if not nums:
        return ''

    n = len(nums)
    if n < 2:
        return nums[0]

    left,right = 0,len(nums)-1
    while left < right:
        mid = left + (right-left)/2
        if nums[mid] > nums[right]:
            left = mid+1
        if nums[mid] < nums[right]:
            right = mid

    return nums[left]
        

case = [[3,4,5,1,2],
        [4,5,6,7,0,1,2],
        [11,13,15,17],
        [1]
        ]
for i in case:
    print i,find_min(i)

