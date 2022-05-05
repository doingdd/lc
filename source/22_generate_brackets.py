#!/usr/bin/python
def gen(n):
    res = []
    
    def dfs(cur_str,left,right):
        if left == 0 and right == 0:
            res.append(cur_str)
            return
        if right < left:
            return

        if left > 0:
            dfs(cur_str+'(',left-1,right)
        if right>0:
            dfs(cur_str+')',left,right-1)

    dfs('',n,n)
    return res
case = [5,4,3,2,1]
for i in case:
    print i,gen(i)
