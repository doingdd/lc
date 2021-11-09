#!/usr/bin/python
def merge_sort(arr):
    if len(arr) < 2:
        return arr

    num = len(arr)/2
    left = merge_sort(arr[:num])
    right = merge_sort(arr[num:])
    arr = merge(left,right)

    return arr

def merge(left,right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    if i < len(left):
        result.extend(left[i:])
    if j < len(right):
        result.extend(right[j:])

    return result
    

case = [[2,3,3,1],[4,3,2,1,0],[1,2,3],[1],[]]
for i in case:
    print i , merge_sort(i)

