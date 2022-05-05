#!/usr/bin/python

case = [
  [[2,3,6,7],7],
  [[2,3,5],8],
  [[2],1],
  [[1],1],
  [[1],2]
]
def combine_sum(candidates,target):
    result = []
    passed = []
    def find(target,passed,candidate):
        if target == 0:
            result.append(passed)
        if target < 0:
            return
        for i,v in enumerate(candidate):
            find(target-v,passed+[v],candidate[i:])

    find(target,passed,candidates)

    return result

for i in case:
    print "case is {0}, result is {1}".format(i,combine_sum(*i))
