#!/usr/bin/python

def check(nums):
    n = len(nums)
    count = 0
    for i in range(n-1):
        if nums[i] > nums[i+1]:
            count += 1

            if i == 0:
                continue

            if nums[i+1] < nums[i-1]:
                nums[i+1] = nums[i]
            else:
                nums[i] = nums[i-1]

        if count > 1:
             return False

    return True




case = [[4,2,3],[3,4,2,3],[1,5,2,4,3],[5,7,1,8]]
for i in case:
  print i,check(i)
