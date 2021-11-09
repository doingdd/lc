#!/usr/bin/python
from collections import defaultdict

def replace_str(s,k):
    s_num = defaultdict(int)
    max_count = 0
    i = 0
    for j,c in enumerate(s):
        s_num[c] += 1
        max_count = max(max_count,s_num[c])
        while j-i+1 > max_count + k: 
            s_num[i] -= 1
            i += 1


    #print s_num['max_count'] 
    return max_count + k


case = [("ABAA",1),
('AAABBBB',2),
('ABCCBD',3),
('ABC',2),
('ABC',0),
('ABC',1),
('BCBCBC',2)
]

for i in case:
  print i,replace_str(*i)
