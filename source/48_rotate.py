#!/usr/bin/python
def rotate(matrix):
    n = len(matrix)
    for i in range(n/2):
        matrix[i],matrix[n-1-i] = matrix[n-1-i],matrix[i]
    for i in range(n):
        for j in range(i,n):
            matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]


matrix = [[1,2,3],[4,5,6],[7,8,9]]
rotate(matrix)
print matrix
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotate(matrix)
print matrix
