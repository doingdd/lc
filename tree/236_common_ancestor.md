# 236. 最近的公共祖先

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。"

## case

![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
```



![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)

```python
输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
```



输入：root = [1,2], p = 1, q = 2
输出：1



## 思路

这道题和一般的二叉树搜索有一点思路上的区别，一般的思路比如求“路径和", ”最大深度"等，很容易想到上层的结果是其下层结果的累加，或者是其它条件，比较容易理解递归的思路。本题是求"祖先",不能说当前节点的"祖先"等于其子节点的"祖先"之和或者累加之类的。

本题的思路是要抛弃原有的思维套路，仅考虑当前节点，如果是满足条件的"祖先",它需要有什么特点：

1.它的左右子节点中，分别包含了p和q

2.它的左右子节点中，有一边包含了q或者q，另一边啥也没包含，但是它本身就是q或者q的其中一个

3.它的左右子节点啥也没包含，由于本题的题干中已经排除了这种情况，所以这个条件无需判断

而遍历过程中返回值也需要确定，一般的二叉树遍历题目中的返回值都和val有关，本题比较特殊，返回值是公共祖先节点本身，也就是说，通过判断当前节点是不是满足了上述的三个条件，满足了就返回当前节点root，它就是最近的"祖先",有可能是p的祖先、q的祖先或者直接就是公共祖先

```python
def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left

        return root
```



## 总结

本题代码简单，思路不太好懂，记住三点：

1. 公共祖先需要满足如下几个情景之一：左右子节点分别包含p和q；左子节点包含p，本身是q；或者反之
2. 遍历时，当前节点的是不是公共祖先，需要返回啥，有四种情况：叶子结点返回空；当前节点match了q或者q之一，就返回当前节点(认为它已经是祖先，不用再往深遍历了，这时它要么q或者q其中之一的祖先，要么是p和q的共同祖先)；left和right子节点都不为空返回root；left和right其中之一为空，则返回另一个(不管它是不是空)



真是绕，先背下来吧
