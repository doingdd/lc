# 79. 单词搜索



## case

示例 1：

![img](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

示例 2：

![img](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

示例 3：

![img](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

## 思路

这种网格问题，又是找路径，很容易想到的套路就是和岛屿问题一样的，深度优先搜索(dfs)

网格问题的基本点：

1. 怎么遍历？已当前节点开始，上下左右四个方向分别遍历
2. 怎么停止？越界停止；word搜索完成则停止
3. 怎么记录？维护一个全局指针，找到一个字母则指针+1，直到指针超出word长度，认为全部找到，在找不到时，退出节点时，指针-1

4. 回溯的防重复，需要记录已经遍历过的节点

```python
def exist(board,word):
    #print board,word
    visited = set()
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    m,n = len(board),len(board[0])
    l = len(word)
    def dfs(i,j,k):
        if board[i][j] != word[k]:
            return False

        if k == l-1:
            return True

        visited.add((i,j))
        find = False
        for x,y in directions:
            newi,newj = i+x,j+y
            if 0 <= newi < m and 0 <= newj < n:
                if (newi,newj) not in visited:
                    find = dfs(i+x,j+y,k+1)
                    if find:
                        return find

        visited.remove((i,j))

        return find

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                find = dfs(i,j,0)
                if find:
                    return find


    return False

for i in range(len(case)):
    print "case is {0},word is {1},result is {2}".format(case[i],word[i],exist(case[i],word[i]))

```



## 总结

这道回溯着实有点麻烦，和岛屿问题相比，它除了正常的dfs以外，要额外处理visited，k这两个全局变量，而且，visited的add和remove的时机很讲究，如果dfs的开始阶段，就是判断停止条件的时候判断(i,j) in visited 则return，答案就错误了。没有想通这是为什么

