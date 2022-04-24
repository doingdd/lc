# 48.旋转图像



## case

![img](https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg)

```python
输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
```

![img](https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg)

输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

## 思路

这道题的思路就是两次对调，一次上下对调，一次沿反对角线对调，没啥可说的，死记就行

```python
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
输出：
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
[[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
```



## 总结

这道题有两点需要注意：

1.翻转的顺序，如果是上下翻转和反对角线翻转，则必须先上下，后对角线，顺序相反得到的结果不对，在实际解题中，先手写下中间步骤，第一次翻转成啥样，第二次翻转成啥样，实际上这一题可以有不同的翻转方式

2.对角线翻转时，里层的循环范围注意是(i,n),而不是从0开始，这是因为只要遍历对角线一边的元素即可，不然就翻转重复了

