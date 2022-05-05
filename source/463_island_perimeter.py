#!/usr/bin/python


case = [
    [
	[0,1,0,0],
	[1,1,1,0],
	[0,1,0,0],
	[1,1,0,0]
    ],
    [[1]],
    [[1,0]],
    [
  	[0,1,0,0],
	[1,1,1,0],
	[0,0,0,0],
	[0,0,0,0]
    ]
]

def perimeter(grid):
    m,n = len(grid),len(grid[0])
    p = 0
    def inArea(i,j):
        return 0 <= i < m and 0 <= j < n

    def dfs(i,j):
        if not inArea(i,j) or grid[i][j] == 0:
            return 1

        if grid[i][j] == 2:
            return 0

        grid[i][j] = 2

        return dfs(i-1,j) +\
               dfs(i+1,j) +\
               dfs(i,j-1) +\
               dfs(i,j+1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                return dfs(i,j)


for i in case:
    print 'case is {0}'.format(i)
    print 'result is {0}'.format(perimeter(i))
