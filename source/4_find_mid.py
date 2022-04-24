#!/usr/bin/python
case = [
    ([1,2],[3,4]),
    ([1,3],[2,4]),
    ([1,3],[2]),
    ([],[1]),
    ([1],[])
    ]

def find_mid(nums1,nums2):
    ## O(m+n)
    i,j = 0,0
    l1,l2 = len(nums1),len(nums2)
    count = (l1+l2)/2 - 1
    while i < l1 or j < l2 and count >= 0:
        count -= 1
        if nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    if (l1 + l2) % 2 == 0:
        return (mid1 + mid2)/2
    else:
        return mid2



for i in case:
    print i,find_mid(*i)
