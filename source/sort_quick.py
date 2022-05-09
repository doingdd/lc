#!/usr/bin/python
case = [
        [5,4,3,2,1],
        [1,2,3,4],
        [1],
        [],
        [1,2,2,2,3,1],
        [1,3,2,4],
        [3,1,2,4]
        ]
def quick_sort(nums):
    if len(nums) < 2:
        return nums

    quick_s(nums,0,len(nums)-1)

    return nums

def partition(nums,left,right):
    i = left
    pivot = nums[left]
    for j in range(left,right+1):
        if nums[j] < pivot:
            nums[j],nums[i] = nums[i],nums[j]
            i += 1

    return i

def quick_s(nums,left,right):
    if left < right:
        p = partition(nums,left,right)
        quick_s(nums,left,p-1)
        quick_s(nums,p+1,right)

for i in case:
    print i,quick_sort(i)
