#!/usr/bin/python
def quick_sort(nums):
    quick_s(nums,0,len(nums)-1)
    return nums

def quick_s(nums,left,right):
    if left < right:
        p = partition(nums,left,right)
        quick_s(nums,left,p-1)
        quick_s(nums,p+1,right)

def partition(nums,left,right):
    pivot = nums[right]
    i = left
    for j in range(left,right):
        if nums[j] < pivot:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
    
    nums[i],nums[right] = nums[right],nums[i]

    return i
        
        
     
case= ([5,2,3,1],
       [5,1,1,2,0,0],
       [1,1],
       [1],
       [3,3,3,3]
       )
for i in case:
    print i,quick_sort(i)
