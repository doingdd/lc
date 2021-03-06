#!/usr/bin/python
def merge_interval(nums):
    nums.sort(key=lambda x:x[0])
    merged = []
    for i in nums:
        if not merged or i[0] > merged[-1][1]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])

    return merged
    
a = ([[1,4],[4,5]],
     [[1,3],[2,6],[8,10],[15,18]],
     [[2,3],[1,2],[3,4],[4,5]]
     )

for i in a:
    print i,merge_interval(i)
