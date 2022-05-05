# 103.二叉树的锯齿形状遍历

## case

给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    	 3
      / \
      9  20
        /  \
       15   7
    返回锯齿形层序遍历如下：
    
    [
      [3],
      [20,9],
      [15,7]
    ]
 ## 思路

本题是锯齿形状，但是其实也是按层的，第一应该想到的就是二叉树的层序遍历，二叉树的层序遍历依赖一个辅助栈

1. 在最开始，把root入栈
2. 然后判断栈的长度，每次取出这个长度的元素，print val后，分别把它的左右子节点入栈(不为空时)
3. 重复第二步，知道栈为空为止

本题在普通程序遍历的基础上有了一个变化，就是之子型遍历，需要额外维护一个level(当前层数)，level为偶数时从做到右，为奇数时从又到左

```python
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque
        if not root:
            return []
        res = []
        level = 0
        queue = deque()
        queue.append(root)
        while queue:
            m = len(queue)
            tmp = []
            for i in range(m):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level % 2 == 1:
                res.append(tmp[::-1])
            else:
                res.append(tmp)

            level += 1
        
        return res
```



## 总结

这道题考查的是层序遍历，记住层序遍历几个点：

1. 辅助stack，初始化存储root
2. 判断stack是否为空，并每次拿出len(stack)个数的节点print，同时将处理的节点的子节点入栈(不为空时)
3. 本题由于加入了反序的变化，需要引入双端队列deque，还有level维护当前层数，来确定每一层结果返回的顺序