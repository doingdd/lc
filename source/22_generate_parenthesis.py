#!/usr/bin/python
def generate(n):
    res = []
    cur_str = ''
    def dfs(cur_str,left,right):
        if left == 0 and right == 0:
            res.append(cur_str)
            return

        if right < left:
            return

        if left > 0:
            dfs(cur_str + '(',left-1,right)
        if right > 0:
            dfs(cur_str + ')',left,right-1)

    dfs(cur_str,n,n)

    return res

case = [1,2,3,4,5]
for i in case:
    print i,generate(i)
