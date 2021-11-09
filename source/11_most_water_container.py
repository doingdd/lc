#!/usr/bin/python

def most_container(nums):
    most_water = 0
    i = 0
    j = len(nums)-1
    while i < j:
        if nums[i] <= nums[j]:
            water = (j - i) * nums[i]
            i += 1
        else:
            water = (j - i) * nums[j]
            j -= 1

        most_water = max(most_water,water)

    return most_water

case = [[1,8,6,2,5,4,8,3,7],
[1,2],
[1,1],
[0,0],
[0,3],
[0,3,4,5,6,7],
[7,8,6,5,4],
[3,3,3,3,3]
]

for i in case:
  print i,most_container(i)
