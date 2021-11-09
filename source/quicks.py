#!/usr/bin/python
def quicks(arr):
    quick_s(arr,0,len(arr)-1)
    return arr

def quick_s(arr,left,right):
    if len(arr) < 2:
        return
    if left < right:
        pi = partition(arr,left,right)
        quick_s(arr,left,pi-1)
        quick_s(arr,pi+1,right)


def partition(arr,left,right):
    i = left
    pivot = arr[right]
    for j in range(left,right):
        if arr[j] < pivot:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1

    arr[i],arr[right] = arr[right],arr[i]

    return i

case = [[],[1],[1,1],[1,2,3],[3,2,1,4],[4,4,3,1,2],[1,4,5,2,3,6,9,10]]
for i in case:
    print i,quicks(i)
