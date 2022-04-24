# 22.括号生成

数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

## case

case = [1,2,3,4,5]

```
输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]
输入：n = 1
输出：["()"]
```

## 思路

这道括号题考查的是回溯，可以先用穷举的思路，它有点像二叉树，从root节点开始，必须先使用左括号，同时向下延伸一个左子节点，使用右括号时延伸一个右子节点，而延伸的条件：

1.右子节点，也就是右括号的个数必须小于左括号，否则会出现`)(`这种，就是无效的

2.左右子节点各能延伸n次

所以采用`减法`的思路，定义两个变量left和right，初始值为n，当减到0时那么遍历结束，返回当前结果

```python
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
```



## 总结

这道题的官方解答很复杂，有用回溯的有用动态规划的，本题采用了一种好理解的，但是时间复杂度比较高的方法，注意几点：

1.dfs遍历的停止条件，一是左右两边的n次都用完(正常返回)，二是右边比左边多延伸了一次，即right<left时

2.dfs时，需要三个变量，cur_str为全局变量，用来存放当前的排列结果。其余两个存放left和right还剩下的额度

3.left或者right >0时，即有额度，就把全局的cur_str加上`(`或者`)`，并且对应的left或者right要-1

干想是想不出来的，硬背吧