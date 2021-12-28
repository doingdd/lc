#!/usr/bin/python

case = [
  ([4,5,6,7,0,1,2],0),
  ([4,5,6,7,0,1,2],3),
  ([1],0),
  ([],0),
  ([1,2,3,0],1),
  ([4,5,6,7,8,1,2,3],8)
]

def bin_search(nums,target):
    if not nums:
        return -1

    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left)/2
        if nums[mid] == target:
            return mid

        if nums[mid] >= nums[0]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < nums[0]:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        
    return -1


for i in case:
    print "case is {0},result is {1}".format(i,bin_search(*i))
