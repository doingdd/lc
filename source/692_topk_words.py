#!/usr/bin/python
import collections
def topk(words,k):
    count = collections.Counter(words)
    sorted_count = sorted(list(count.items()),key=lambda x: (-x[1],x[0]))
    return sorted_count[:k]

case = [(["the",'day','is','sunny','is','sunny','the','the'],2),
        (['i','love','coding','i','love'],2)
       ]
for i in case:
    print i,topk(*i) 
