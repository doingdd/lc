# 112. 路径总和



## case

![img](https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg)

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。



## 思路

这道题最开始想到的一定是递归遍历了，由于是计算和，是进入每个节点的时候累加当前节点的值，所以应该是前序遍历，但是仍然由于细节问题fail了，那就是[1,2]这种二叉树，targetsum=1时，左子树显然是不满足条件的，右子树为空，如果把空也算成子树的话，叶子节点其实就是根节点本身，这样算应该是满足条件的，但是leetcode的case要求返回False，不满足，也就是根节点就是根节点，叶子节点就是叶子结点

标准写法，背下来吧：

```python
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == targetSum
        
        return self.hasPathSum(root.left,targetSum-root.val) or self.hasPathSum(root.right,targetSum-root.val)
```

二刷，有了另一个写法，核心还是targetSum-root.val，只不过应用了前序遍历的思路，就是在刚刚进入节点的时候将减法做了，然后将减后的target值传给left和right, 需要注意的是，这两种写法其实都有一个重要思路：就是左子树或者右子树只要有一个满足条件就可以，所以dfs(root.left) or dfs(root.right)这个“or"非常重要

```python
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root,target):
            if not root:
                return False
            target -= root.val
            if target == 0 and (not root.left) and (not root.right):
                return True 
            return dfs(root.left,target) or dfs(root.right,target)
        
        return dfs(root,targetSum)
```



## 总结

这道题虽然是简单题，但是也包含了二叉树核心的遍历的灵活运用，二叉树的dfs遍历框架，前中后序三种方式，需要根据题目要求灵活选择，比如本题是要求和，那就要再进入节点的时候操作

1. 注意对root为空的判断，初始为空直接返回，由深度递归遍历传进来的root为空，则提前判断，其实也就是提前判断叶子节点是否已经遍历到了，这个操作在普通的遍历里还是不常见的，一般的遍历，直接会遍历到叶子节点的left或者right为止，相当于比本题中多遍历一层
2. return的设置，本题是有满足条件的返回即可，所以用了“or”，这个return其实也同时完成了二叉树的前序遍历的后半部分

