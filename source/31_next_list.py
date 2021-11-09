#!/usr/bin/python

def next_list(nums):
    l = len(nums)
    i = l - 2
    while i >= 0:
        if nums[i] < nums[i+1]:
            break
        i -= 1

    if i >= 0:
        j = l - 1
        while nums[i] > nums[j]:
            j -= 1
        
        nums[i],nums[j] = nums[j],nums[i]

    nums[i+1:] = nums[:i:-1] if i >= 0 else nums[::-1]

    return nums


case = ([1,2,3],
        [3,2,1],
        [1,3,2],
        [4,5,2,6,3,1],
        [1,3,2,4]
        )

for i in case:
    print i,next_list(i)

