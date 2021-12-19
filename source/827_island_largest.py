#!/usr/bin/python

case = [
  [
   [1,0],
   [0,1]
  ],
  [
    [1,1],
    [1,0]
  ],
  [
   [0,1,0,0],
   [1,1,1,0],
   [0,0,0,0],
   [1,1,0,0]
  ],
  [
    [1,1],
    [1,1]
  ],
  [
    [0,0],
    [0,0]
  ],
  [[0]],
  [[0,1]]
]

def island_largest(grid):
    m,n = len(grid),len(grid[0])
    area_list = []
    flag = True
    def inArea(i,j):
        return 0 <= i < m and 0 <= j < n

    def dfs(i,j,flag):
        if not inArea(i,j):
            return 0,flag

        if grid[i][j] == 2:
            return 0,flag

        if grid[i][j] == 0:
            if flag:
                flag = False
            else:
                return 0,flag

        area = 1
        if grid[i][j] == 1:
            grid[i][j] = 2

        ans,flag = dfs(i-1,j,flag)
        area += ans
        ans,flag = dfs(i+1,j,flag)
        area += ans
        ans,flag = dfs(i,j-1,flag)
        area += ans
        ans,flag = dfs(i,j+1,flag)
        area += ans

        return area,flag

    for i in range(m):
        for j in range(n):
            flag = True
            area,flag = dfs(i,j,flag)
            print area,flag
            area_list.append(area)


    return max(area_list) if area_list else 0

for i in case:
    print 'case is {0}'.format(i)
    print 'result is {0}'.format(island_largest(i))
