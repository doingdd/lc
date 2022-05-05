#!/usr/bin/python
def longest_s(s):
    def find_s(s,l,r):
        while l >=0 and r <len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return l+1,r-1

    if not s:
        return 0

    length = len(s)
    sub_l = 0
    left,right = 0,0
    for i in range(length):
        l1,r1 = find_s(s,i,i)
        if r1-l1+1 > sub_l:
            sub_l = r1-l1+1
            left,right = l1,r1
        l2,r2 = find_s(s,i,i+1)
        if r2-l2+1 > sub_l:
            sub_l = r2-l2+1
            left,right = l2,r2

    #print left,right

    return s[left:right+1]

        

case = ["abba",'a','aa','','abc','abccba','abbcdc','abbcd','babad','cbbd']
for i in case:
    print i,longest_s(i)
