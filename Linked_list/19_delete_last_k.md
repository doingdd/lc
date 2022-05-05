# 19. 删除链表的倒数第N个节点

给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

## case

![img](https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg)

```
输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
```

```
head = [1], n = 1
输出[]
```

```
输入：head = [1,2], n = 1
输出：[1]
```

## 思路

一次遍历的话就是双指针，倒数第n个就是让快指针和慢指针间隔n，然后快指针指向尾结点时，慢指针的位置的next删掉就可以了

需要考虑的特殊情况就是删除的节点为head的时候，本题中由于给定了条件n不会大于链表长度，所以可以根据第一次遍历n结束后，快指针的位置来判断是不是需要删除头结点head



```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = head
        while n > 0 and p:
            p = p.next 
            n -= 1
        ## 如果n恰好等于链表长度，也就是说需要删除head节点时，p在走了n步之后应该恰好等于None  
        if not p:
            new_head = head.next
            head.next = None
            return new_head 

        while p.next:
            p = p.next
            q = q.next 

        q.next = q.next.next 
        return head
```



Dummy 解法：

```python
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0,head)
        q = head 
        p = dummy
        for i in range(n):
            q = q.next 
        
        while q:
            p = p.next 
            q = q.next
        
        p.next = p.next.next 
        return dummy.next 
```



## 总结

本题需要注意的就是双指针的思路，还有特殊情况的处理

特殊情况1. 链表为空

特殊情况2：n恰好等于链表长度，也就是要删除的节点是头结点

特殊情况3：n大于链表长度，本题题干已经限制了这个情况的出现

为了进一步简化特殊情况2带来的代码不整洁，可以使用哨兵节点，就是给链表一个空的虚拟节点dummy,可以看到dummy节点的引入既不用判断特殊情况1，也不用判断特殊情况2，dummy需要注意的点：

1. 慢指针指向dummy，快指针指向head，实际上快慢指针天然就多了一步的差距，所以在第二次循环到尾结点的时候，采用的条件是while p, 不是第一种不带dummy写法的while p.next,相当于多走了一步，这一步非常关键，最好在纸上画出几个例子过一遍