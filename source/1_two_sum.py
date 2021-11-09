#!/usr/bin/python

def two_sum(nums,target):
    target_idx = {}
    for i,v in enumerate(nums):
        k = target - v
        if v not in target_idx:
            target_idx[k] = i
        else:
            return [target_idx[v],i]

    return []


case = (([2,7,11,5],9),
        ([3,2,4],6),
        ([3,3],6),
        ([3,2],7)
        )

for i in case:
    print 'case is :{0},result is: {1}'.format(i,two_sum(*i))

