#!/usr/bin/python

case = (
	[
	    ["1","1","1","1","0"],
	    ["1","1","0","1","0"],
	    ["1","1","0","0","0"],
	    ["0","0","0","0","0"]
	],
        [
  	    ["1","1","0","0","0"],
  	    ["1","1","0","0","0"],
  	    ["0","0","1","0","0"],
  	    ["0","0","0","1","1"]
	],
        [
  	    ["1","1","0","0","1"],
  	    ["1","0","0","1","0"],
  	    ["0","1","1","0","0"],
        ],
        []
)
def numIsland(grid):
    '''type grid: List[List[str]]
       type rt: int
    '''
    def inArea(i,j):
        return i>=0 and j>=0 and i<m and j<n

    def dfs(i,j):
        #if not inArea(i,j):
        if not 0 <= i < m or not 0 <= j < n:
            return 
        if grid[i][j] != "1":
            return

        grid[i][j] = 2
        dfs(i-1,j)
        dfs(i+1,j)
        dfs(i,j-1)
        dfs(i,j+1)


    if not grid:
        return 'Invalid'

    count = 0
    m,n = len(grid),len(grid[0])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                dfs(i,j)
                count += 1

    return count


for i in case:
    print 'case is {0},result is {1}'.format(i,numIsland(i))
