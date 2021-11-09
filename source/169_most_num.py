#!/usr/bin/python

def most_num(nums):
    if not nums:
        return ''

    n = len(nums)
    if n < 2:
        return nums[0]

    nums.sort()
    return nums[n/2]

def most_num1(nums):
    if not nums:
        return ''

    n = len(nums)
    if n < 2:
        return nums[0]

    m = None
    c = 0
    for i in nums:
        if c == 0:
            m = i

        if i != m:
            c -= 1

        else:
            c += 1

    return m

    

case = ([3,2,3],
        [2,2,1,1,1,2,2],
        [1,1,2,2,2,2,1],
        [1],
        [1,1]
        )
for i in case:
    print i,most_num1(i)
