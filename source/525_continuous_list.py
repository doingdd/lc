#!/usr/bin/python
def max_len(nums):
    count = 0
    count_idx = {0:-1}
    max_l = 0
    for i,v in enumerate(nums):
        count += 1 if v == 1 else -1
        if count in count_idx:
            max_l = max(max_l,i-count_idx[count])
        else:
            count_idx[count] = i
        

    return max_l


case = ([0,1],
        [0,1,0],
        [0,0,1,1],
        [1,0,0,0,1,1,1],
        [0,1,0,1,0,0,1],
        [0,0,1,0,0]
        )
for i in case:
    print i,max_len(i)
