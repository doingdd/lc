#!/usr/bin/python
def insert_sort(arr):
    for j in range(1,len(arr)):
        i = j - 1
        val = arr[j]
        while i >= 0:
            if val < arr[i]:
                arr[i+1] = arr[i]
                arr[i] = val

            i -= 1

    return arr

case = [[2,3,3,1],[1,3,4],[3,2,1],[],[1,1,1]]
for i in  case:
    print i,insert_sort(i)
