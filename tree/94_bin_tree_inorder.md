# 94. 中序遍历

给定一个二叉树的根节点 root ，返回它的 中序 遍历。

 

示例 1：

<img src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" alt="img" style="zoom:50%;" />

输入：root = [1,null,2,3]
输出：[1,3,2]

示例 2：

输入：root = []
输出：[]

## 思路

二叉树的前中后序遍历的递归基本框架：

```python
if root:
  ## 前序遍历在这里处理逻辑, res.append(root.val)
  dfs(root.left)
  ## 中序遍历在这里处理逻辑, res.append(root.val)
  dfs(root.right)
  ## 后续遍历在这里处理逻辑, res.append(roo.val)
```

本题的解法：

```python
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def dfs(root):
            if not root:
                return []
            
            dfs(root.left)
            self.res.append(root.val)
            dfs(root.right)
        
        self.res = []
        dfs(root)
        return self.res
```

## 总结

注意框架思路，很多二叉树的问题，核心要解决的就是在什么位置处理逻辑的问题，比如543.树的直径，就是利用了后序遍历，将遍历后的结果做处理的思路

二叉树的问题，核心就是**如何遍历+如何递归(分解)**的问题

