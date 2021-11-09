#!/usr/bin/python

def up(arr):
    c_idx = len(arr) - 1
    p_idx = (c_idx - 1)/2
    temp = arr[c_idx]
    while c_idx > 0 and temp < arr[p_idx]:
        arr[c_idx] = arr[p_idx]
        c_idx = p_idx
        p_idx = (p_idx - 1)/2

    arr[c_idx] = temp

def down(arr,p_idx):
    c_idx = 2*p_idx + 1
    temp = arr[p_idx]
    l = len(arr)
    while c_idx < l:
        if c_idx + 1 < l and arr[c_idx+1] < arr[c_idx]:
            c_idx += 1

        if temp <= arr[c_idx]:
            break

        arr[p_idx] = arr[c_idx]
        p_idx = c_idx
        c_idx = 2*c_idx + 1

    arr[p_idx] = temp

def build(arr):
    i = (len(arr) - 1 - 1)/2
    while i >= 0:
        down(arr,i)
        i -= 1

    return arr

case = [[8,3,2,2,3,4,5,6,7]]
for i in case:
    print i,build(i)
