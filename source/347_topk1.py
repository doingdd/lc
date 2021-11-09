#!/usr/bin/python
def down(arr,p_idx):
    l = len(arr)
    c_idx = p_idx * 2 + 1
    tmp = arr[p_idx]
    while c_idx < l:
        if c_idx+1 < l and arr[c_idx+1][1]<arr[c_idx][1]:
            c_idx += 1
        if tmp[1] <= arr[c_idx][1]:
            break

        arr[p_idx] = arr[c_idx]
        p_idx = c_idx
        c_idx = p_idx * 2 + 1

    arr[p_idx] = tmp

def build(arr):
    i = (len(arr) -2) /2
    while i >= 0:
        down(arr,i)
        i -= 1

    return arr

def top_k(nums,k):
    k_nums = {}
    if k < 1:
        return []

    if k > len(nums):
        return nums

    for i in nums:
        k_nums[i] = k_nums.get(i,0) + 1

    heap_k = build(k_nums.items()[:k])
    for j in k_nums.items()[k:]:
        if j[1] <= heap_k[0][1]:
            continue
        heap_k[0] = j
        down(heap_k,0)

    return [i[0] for i in heap_k]

case = [([1,2,3,3,4],1),
        ([1,2,3,3,4],2),
        ([1],1),
        ([3,2,4,2,1,2,3],3),
        ([3,2,4,2,1,2,3],7),
        ([],1),
        ([1,2,2],5),
        ([1,2,2],0)
        ]

for i in case:
    print i,top_k(*i)
