# 剑指55.2 判断平衡二叉树

输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

## case

```
  	3
   / \
  9  20
    /  \
   15   7
```

返回 `true` 。

```
   		 1
      / \
     2   2
    / \
   3   3
  / \
 4   4
```

返回 `false` 。

## 思路

平衡二叉树的定义是左右子树深度相差不超过1，这里的核心，是如何在遍历的过程中，求得每个节点的左右子树的高度，并判断差值

求左右子树的高度是offer 55.1题目的考查点，核心思路就是后序遍历的递归，当前节点的深度是其左右子树深度最大值+1，然后在每次遍历时计算深度差，如果大于1则直接返回False,如下写法，虽然比较丑陋，但是容易理解 

```python
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            if left is False:
                return False
            right = dfs(root.right)
            if right is False:
                return False
            
            if abs(left-right) > 1:
                return False
            
            return max(left,right) + 1
        
        if dfs(root) is False:
            return False
        
        return True
```



## 总结

这道题与求最大深度类似，求最大深度需要注意的点

1. root为空时，返回0
2. 不为空时，返回max(left,right) + 1
3. 本题中额外需要判断每个left和right的差值，不满足条件时需要把False传出来