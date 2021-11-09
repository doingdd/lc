#!/usr/bin/python
def first_k(arr,k):
    if k > len(arr):
        return arr

    dict_k = {}
    for i in arr:
        dict_k[i] = dict_k.get(i,0) + 1

    sorted_k = sorted(dict_k.keys(),key=lambda x:dict_k.get(x),reverse=True)
  
    return sorted_k[:k]

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
    print i,first_k(*i)
