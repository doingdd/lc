# 89 删除链表重复元素

## 思路

思路很简单，就是遍历的时候判断当前节点的值与下一节点值是否相等即可

难点在于边界值的处理，在代码实现的时候，由于在遍历的过程中既删除又往前走，很容易走到None，导致代码运行失败，这里的写法有一些弯：

```python
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        p = head
        while p and p.next:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return head 
```

首先while的终止条件是p.next，因为只要遍历到最后一个节点即可，不用判断到None

其次这里判断两个节点相等时，只是删除了一个节点，并没有将指针往前走，而是在下一轮循环里自动走入else分支，往前继续遍历。这个写法避免了结尾是三个连续节点出现的异常，比如[1,1,1]这种，如果不加这个else，每次都往前走，那么三个节点相等时，会少删除一个节点。这一点一定注意

## 总结

本题思路简单，实现也简单，但是边界值判断这一个坑还是很容易出现绕不出去的情况，死记硬背注意吧