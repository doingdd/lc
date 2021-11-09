#!/usr/bin/python

def find_target(matrics,target):
    if not matrics:
        return False

    len_i = len(matrics)
    len_j = len(matrics[0])
    i = 0
    j = len_j-1
    while i < len_i and j >=0:
        if matrics[i][j] == target:
            return True
        if matrics[i][j] < target:
            i += 1
        else:
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
