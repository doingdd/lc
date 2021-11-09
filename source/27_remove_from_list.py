#!/usr/bin/python

def removeFromList(nums,val):
    i = j = 0
    while j < len(nums):
        if nums[j] != val:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j += 1
        else:
            j += 1

    return len(nums[:i])
        



nums = []
val = 1
print nums,val,removeFromList(nums,val),nums

nums = [0]
val = 0
print nums,val,removeFromList(nums,val),nums

nums = [0,1,1]
val = 1
print nums,val,removeFromList(nums,val),nums

nums = [0,1,2]
val = 2
print nums,val,removeFromList(nums,val),nums

nums = [0,0,0]
val = 0
print nums,val,removeFromList(nums,val),nums

nums = [0,1]
val = 0
print nums,val,removeFromList(nums,val),nums

nums = [0,1,2,3,4,5]
val = 2
print nums,val,removeFromList(nums,val),nums

nums = [0,1,2,2,3,8,10,2,4,4,5]
val = 2
print nums,val,removeFromList(nums,val),nums

