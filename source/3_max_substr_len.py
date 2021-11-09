#!/usr/bin/python

def sub_str(s):
    length = len(s)
    len_sub = 0
    if len(s) < 2:
        return len(s)

    start,end = 0,1
    while end < length:
        if (len(set(s[start:end+1])) == len(s[start:end+1])):
            len_sub = max(len_sub,len(s[start:end+1]))
            end += 1
        else:
            start += 1

    return len_sub
def sub_str1(s):
    length = len(s)
    len_sub = 0
    if len(s) < 2:
        return len(s)

    start,end = 0,0
    sub_set = set()
    while end < length:
        if s[end] not in sub_set:
            len_sub = max(len_sub,len(s[start:end+1]))
            sub_set.add(s[end])
            end += 1
        else:
            sub_set.remove(s[start])
            start += 1

    return len_sub

case = ["paweww","ab","abcd","",'c',"aaa","aa","abcab",'abb']
for i in case:
    print i,sub_str1(i)


