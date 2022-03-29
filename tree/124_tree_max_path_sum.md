# 124.最大路径和

## case

路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

![img](https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg)

```python
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

```



![img](https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg)

```python
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42
```



## 思路

这道题的遍历方式属于后序遍历，也就是说，遍历每个树的节点时，它的路径和其实取决于它的子节点

整体思路就是遍历+递归，遍历的时候，得到每个节点的"最大路径和"，也就是假设一个一定经过该节点的路径，并得出它的路径和，这样再加上维护一个全局变量maxSum,一遍遍历一遍更细腻maxSum即可

那么怎么得到每个节点上的"最大路径和"呢？经过观察不难得出，每个节点的最大路径和等于**它左子节点的相对和+当前节点+右子节点的相对和**(官方解答给子节点的相对和起了个名字：最大贡献值)，而每个子节点的**最大贡献值**又等于max(left,right) 与子节点值的和(这里需要判断max(left,right)是不是小于0，如果小于0就废弃掉，仅保留节点本身的value)

所以这个最大路径和从底向上有**三层**:

1. root为空时，无贡献，返回0
2. 左子节点的最大贡献值：left = max(root.left,0)，右子节点最大贡献值:right = max(root.right,0)，当前节点最大贡献值:max(left,right) + root.val
3. 当前节点的最大路径和: left + right + root.val,注意这里left或right可能为0(因为他们小于零无贡献)

实现如下：

```python
class Solution(object):
    def __init__(self):
        self.maxSum = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            cur = left + root.val + right
            self.maxSum = max(cur,self.maxSum)
            sub_max = max(left,right)
            cur_max = root.val + sub_max if root.val + sub_max > 0 else 0
            return cur_max 
        
        dfs(root)
        return self.maxSum 
```

官方答案的写法更简洁，相当于再left和right的取值时把小于0的给排除掉了

```python
def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def dfs(root):
            if not root:
                return 0
            left = max(dfs(root.left),0)
            right = max(dfs(root.right),0)
            cur = left + right + root.val
            self.maxSum = max(cur,self.maxSum)
            return max(left,right) + root.val
```

在解释一下为什么root.val小于0的情况不考虑，而left和right即左右子节点小于0都舍弃了，因为遍历的过程有一个前提：就是路径必须经过当前节点，即使这个节点值为负，也不过就是多算了一次，但是保证了每个路径都被计算过了

## 总结

这道题代码简单，但是思路想要捋顺了还是有一些麻烦，首先要有”节点贡献值”的概念，即遍历每个节点，然后在计算的过程中有三层思路：

1. root为空时
2. root不为空，计算左右子节点的贡献值时,有两层max：max(dfs(root.left),0),max(dfs(root.right),0), max(left,right) + root.val
3. 路径和，由于在2中已经对小于0做了取舍，这里就很简单相加即可:left +right + root.val

