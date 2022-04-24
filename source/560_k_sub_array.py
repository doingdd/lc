#!/usr/bin/python
def sub_array_num(nums,k):
    pre_sum = {0:1}
    cur_sum = 0
    count = 0
    for i in nums:
        cur_sum += i
        if (cur_sum-k) in pre_sum:
            count += pre_sum[cur_sum-k]

        pre_sum[cur_sum] = pre_sum.get(cur_sum,0) + 1

    return count
            
case = [
        ([1,1,1],1),
        ([1,1,1],2),
        ([1,2,3],3),
        ([1,2,3],4),
        ([5,1,4,-1,1,2,3],5),
        ([],1),
        ([1],1),
        ([2],1)
        ]
for i in case:
    print i,sub_array_num(*i)
