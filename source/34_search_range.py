#!/usr/bin/python

case = [
  ([5,7,7,8,8,10],8),
  ([5,7,7,8,8,10],6),
  ([],0),
  ([1,1,1,1],1),
  ([1,1,1,1],0),
  ([1,2,3,4,5,6,6],6),
  ([1,1,2,3,4,5,6,6],1)
]

def search_range(nums,target):
    i,j = -1,-1
    if not nums:
        return [i,j]

    left,right = 0,len(nums)-1
    while left <= right:
        mid = left + (right-left)/2
        if target == nums[mid]:
            i,j = find_range(0,len(nums)-1,nums,mid)
            break
        elif target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1


    return [i,j]

def find_range(left,right,nums,mid):
    i,j = mid,mid
    while i >=left and nums[i] == nums[mid]:
        i -= 1

    while j <= right and nums[j] == nums[mid]:
        j += 1

    return i+1,j-1


for i in case:
    print "case is {0}, result is {1}".format(i,search_range(*i))
