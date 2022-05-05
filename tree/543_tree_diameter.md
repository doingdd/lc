# 543. 二叉树的直径



## 用例

```
  				1
         / \
        2   3
       / \     
      4   5    
```

返回 **3**, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

## 思路

这个题考查的是二叉树的遍历，二叉树的问题都离不开遍历，这类题目跟岛屿类题目一样，有两个要点：

1. 如何遍历
2. 如何再遍历的时候处理逻辑

这道题，可以采用分解子问题的方法，每个节点的直径，都等于其左子树的最大深度+右子树的最大深度之和，而在遍历的同时，将当前节点的直径(左右子树深度之和)与全局的最大直径做对比，实时更新最大直径

这里仅列出核心处理的函数，树的构造以及case的运行后面再实现

```python
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = 0
        self.dfs(root)
        
        return self.max

    def dfs(self,root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.max = max((left+right),self.max)

        return max(left,right) + 1
```



## 总结

这是一个基础的二叉树遍历问题，有几个要点：

1. 全局变量存储当前的最大直径
2. 遍历时，由于依赖子问题的返回结果，所以是后续遍历，也就是在遍历完成left和right的基础上，将其返回值做处理之后，再返回
3. 子问题的分解，本题分解为左子树的高度和右子树的高度的最大值，这一点很重要，因为求的是最大直径，所以左右子树其实只有一个可以保留高度，为其父节点所用来计算直径，也就是max(left,right) + 1
4. 左子树的高度定义：这里其实包含了root的子节点，和root节点本身，也就是说，子树的高度，不是从子节点开始算的，是从当前节点本身开始计算的