#!/usr/bin/python
def find_combine(candidates,target):
    passed_list = []
    def combine(target,passed,candidate):
        if target < 0:
            return

        if target == 0:
            passed_list.append(passed)
        for i,v in enumerate(candidate):
            combine(target-v,passed+[v],candidate[i:])

    combine(target,[],candidates)
    return passed_list

candidates_target = [([2,3,6,7],7),
  ([2,3,5],8),
  ([2],8),
  ([1,2,3,4],10)
  ]
for i in candidates_target:
    print i,find_combine(*i)
    

