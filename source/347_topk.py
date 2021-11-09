#!/usr/bin/python
def down(arr,p_idx):
    l = len(arr)
    c_idx = 2*p_idx + 1
    temp = arr[p_idx]
    while c_idx < l:
        if c_idx + 1 < l and arr[c_idx+1][1] < arr[c_idx][1]:
            c_idx += 1

        if temp[1] < arr[c_idx][1]:
            break

        arr[p_idx] = arr[c_idx]
        p_idx = c_idx
        c_idx = 2*c_idx + 1

    arr[p_idx] = temp

def build(arr):
    i = (len(arr)-2)/2
    while i>=0:
        down(arr,i)
        i -= 1

    return arr

def top_k(arr,k):
    dict_fre = {}
    for i in arr:
        dict_fre[i] = dict_fre.get(i,0) + 1

    list_fre = list(dict_fre.items())
    heap_k = build(list_fre[:k])
    for i in list_fre[k:]:
        if i[1] > heap_k[0][1]:
            heap_k[0] = i
            down(heap_k,0)

    return [i[0] for i in heap_k]


case = [([1,1,1,2,2,3],2),
        ([1],1)
       ]

for i in case:
    print i,top_k(*i)

