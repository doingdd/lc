#!/usr/bin/python
from collections import deque

def max_sliding(nums,k):
    if k == 1:
        return nums

    rt_list = []
    q = deque()
    i = 0

    for j,v in enumerate(nums):
        while q and q[-1] < v:
            q.pop()

        q.append(v)
        if j-i >= k-1:
            rt_list.append(q[0])
            if nums[i] == q[0]:
                q.popleft()
            
            i+=1

    return rt_list


k = 3
case = (
[ -1,1,3,4,8,-14],
[1,23,4,2,3,4,5,6,12,2,1,1],
[1,1,1,1,1,1],
[0],
[],
[9,8,7,6,5,4,3,2,1,0,0],
[0,1,2,3,4,5,4,3,2,1,10]
)

for i in case:
    print max_sliding(i,k)

