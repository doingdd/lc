#!/usr/bin/python
def duplicate_num(nums):
    duplicate_nums = []
    for v in nums:
        real_v = abs(v)
        if nums[real_v-1] < 0:
            duplicate_nums.append(real_v)
        nums[real_v-1] = -nums[real_v-1]

    return duplicate_nums


case = ([4,3,2,7,8,2,3,1],
        [],
        [1,1,1,1],
        [1,2,3],
        [5,2,2,1,5]
        #[0,1,3,1,0]
        )
for i in case:
    print i,duplicate_num(i)
