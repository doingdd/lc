#!/usr/bin/python
def quicks(arr):
    quick_s(arr,0,len(arr)-1) 
    return arr

def quick_s(arr,start,end):
    if len(arr) < 2:
        return

    if start < end:
        p = partition(arr,start,end)
        quick_s(arr,start,p-1)
        quick_s(arr,p+1,end)

def partition(arr,start,end):
    pi = arr[end]
    i = start
    for j in range(start,end):
        if arr[j] < pi:
            arr[i],arr[j] = arr[j],arr[i]
            i += 1

    arr[i],arr[end] = arr[end],arr[i]

    return i

a = [[0,1,3,4],[],[4,3,1],[3,2,2,1,0],[2,2,2],[1],[1,1],[1,3,2,5,4,6,8,7]]
for i in a:
  print i,quicks(i)
