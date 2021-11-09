#!/usr/bin/python
def down(arr,p_idx):
    l = len(arr)
    c_idx = p_idx * 2 + 1
    tmp = arr[p_idx]
    if not 
    while c_idx < l:
        if c_idx+1 < l and arr[c_idx+1]<arr[c_idx]:
            c_idx += 1
        
        if tmp <= arr[c_idx]:
            break

        arr[p_idx] = arr[c_idx]
        p_idx = c_idx
        c_idx = 2*c_idx + 1

    arr[p_idx] = tmp

def fisrtk(arr,k):
    if k < 1 or k > len(arr):
        return 

    heap_k = []
    for i in arr:
        if heap and

case = [
       ([1,2,3,4,4],1),
       ([1,2,3,4,4],2),
       ([3,2,1,5,6,4],2),
       ([3,2,3,1,2,4,5,5,6],4)
       ]

for i in case:
    print i,firstk(*i)

