#!/usr/bin/python
case = [
 [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
 ],
 [[0,0,0,0,0,0,0,0]],
 [
  [0,1,0,0],
  [1,1,1,0],
  [0,1,0,0],
  [1,1,0,0]
 ]
]

def max_area(grid):
    m,n = len(grid),len(grid[0])
    def inArea(i,j):
        return 0 <= i < m and 0 <= j < n

    def dfs(i,j):
        if not inArea(i,j) or grid[i][j] != 1:
            return 0 

        grid[i][j] = 2
        area = 1
        area += dfs(i-1,j)
        area += dfs(i+1,j)
        area += dfs(i,j-1)
        area += dfs(i,j+1)

        return area

    area_list = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                area = dfs(i,j)
                area_list.append(area)

    return max(area_list) if area_list else 0

for i in case:
    print 'case is {0}'.format(i),
    print 'reuslt is {0}'.format(max_area(i))
