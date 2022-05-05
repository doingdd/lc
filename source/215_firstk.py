#!/usr/bin/python
def down(arr,p_idx):
    pass
import heapq
def firstk(nums,k):
    if not nums:
        return None
    heap = nums[:k]
    heapq.heapify(heap)
    print( heap)
    for i in nums[k:]:
        if i >= heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,i)

    return heap[0]

case = [
       ([1,2,3,4,4],1),
       ([1,2,3,4,4],2),
       ([3,2,1,5,6,4],2),
       ([3,2,3,1,2,4,5,5,6],4)
       ]

for i in case:
    print i,firstk(*i)

