#!/usr/bin/python
def duplicate_num(nums):
    result = []
    l = len(nums)
    for i in range(l):
        v = abs(nums[i])
        if nums[v-1] < 0:
            result.append(v)
        else:
            nums[v-1] = -nums[v-1]

    return result
case = ([4,3,2,7,8,2,3,1],
        [],
        [1,1,1],
        [1,2,3],
        [5,2,2,1,5]
        #[0,1,3,1,0]
        )
for i in case:
    print i,duplicate_num(i)
