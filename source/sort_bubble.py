#!/usr/bin/python
case = [
        [5,4,3,2,1],
        [1,2,3,4],
        [1],
        [],
        [1,2,2,2,3,1],
        [2,3,1]
        ]
def bubble_sort(nums):
    l = len(nums)
    for i in range(l):
        for j in range(i,l):
            if nums[i] > nums[j]:
                nums[i],nums[j] = nums[j],nums[i]

    return nums

for i in case:
    print i,bubble_sort(i)
