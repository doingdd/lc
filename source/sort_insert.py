#!/usr/bin/python
case = [
        [5,4,3,2,1],
        [1,2,3,4],
        [1],
        [],
        [1,2,2,2,3,1],
        [1,3,2,4]
        ]
def insert_sort(nums):
    l = len(nums)
    for i in range(1,l):
        value = nums[i]
        j = i-1
        while j >= 0:
            if nums[j] > value:
                nums[j+1] = nums[j]
            else:
                break

            j -= 1

        nums[j+1] = value

    return nums

for i in case:
    print i,insert_sort(i)




