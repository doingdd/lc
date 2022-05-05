#!/usr/bin/python
case = [
 [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
 ],
 [
  ["a"]
 ],
 [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
 ]
]
word = ["ABCCED","a","ABCB"]

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
