# 二叉树的最大深度



## case

给定二叉树 [3,9,20,null,null,15,7]，

    	 3
    	/ \
      9  20
        /  \
       15   7

返回它的最大深度 3 。

## 思路

求深度，和112求路劲和很像，都已从递归+题目分解入手，即当前节点的深度，等于其左右子树深度的最大值+1

```python
   def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if not root else max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
```



## 总结

这道题基本就是记忆题，记住了基本套路：当前节点的xx等于它左子树或右子树的xx累加而来，就行了

