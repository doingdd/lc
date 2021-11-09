#!/usr/bin/python
from collections import defaultdict

def str_include(s1,s2):
    len_s = len(s1)
    i = 0
    j = len_s
    dict_s1 = defaultdict(int)
    dict_s2 = defaultdict(int)
    for c in s1:
        dict_s1[c] += 1

    for c in s2[i:j]:
        dict_s2[c] += 1

    if dict_s1 == dict_s2:
        return True

    while j <= len(s2):
        #print dict_s1,dict_s2
        if dict_s1 != dict_s2:
            dict_s2[s2[i]] -= 1
            if not dict_s2[s2[i]]:
                dict_s2.pop(s2[i])

            i += 1
            j += 1
            if j <= len(s2):
                dict_s2[s2[j-1]] += 1
        else:
            return True

    return False

case = [('ab','ffeddbac'),
('ab','fadfffffbsda'),
('ab','bcab'),
('aaa','baaa'),
('aaa','baa'),
('abc','a'),
('abcdefg','abcdegfedcba')
]

for i in case:
    print i,str_include(*i)

