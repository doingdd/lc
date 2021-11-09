#!/usr/bin/python

def find_target(matrics,target):
    m = len(matrics[0])
    n = len(matrics)
    i,j = 0,m-1
    while i<n and j>=0:
        if target == matrics[i][j]:
            return True
        elif target > matrics[i][j]:
            i += 1
        elif target < matrics[i][j]:
            j -= 1

    return False

case = ([[1,3,5,7],
         [10,11,16,20],
         [23,30,34,60]],3)
print case,find_target(*case)

case = ([[1,3,5,7],
         [10,11,16,20],
         [23,30,34,60]],13)
print case,find_target(*case)
