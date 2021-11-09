#!/usr/bin/python

def removeDuplicate(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[j] == nums[i]:
            j += 1
        else:
           i += 1
           nums[i],nums[j] = nums[j],nums[i]
           j += 1

    
    return len(nums[:i+1])




nums = [0,1,1]
print nums,removeDuplicate(nums),nums

nums = [0,0,1]
print nums,removeDuplicate(nums),nums

nums = [0,1]
print nums,removeDuplicate(nums),nums

nums = [0]
print nums,removeDuplicate(nums),nums

nums = [1,1,1]
print nums,removeDuplicate(nums),nums

nums = [0,1,1,2,2,2,2,3]
print nums,removeDuplicate(nums),nums

nums = [0,5,6,6,7]
print nums,removeDuplicate(nums),nums

nums = []
print nums,removeDuplicate(nums),nums
