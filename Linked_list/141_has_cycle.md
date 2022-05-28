# 141.环形链表

给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

## case

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

## 

## 思路

快慢指针，快指针q每次移动两步，慢指针p每次移动一步,如果链表没环，那么q肯定会遇到None；如果有环，那么q迟早会年上p，也就是p == q

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        
        p = head
        q = head
        while q.next and q.next.next:
            q = q.next.next
            p = p.next 
            if p == q:
                return True

        return False 
```

补充一个带哨兵的写法,带上哨兵之后，初始值p和q分别等于pre和pre.next(head), 省去了判断head为空的情况

```python
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre = ListNode(None)
        pre.next = head
        p,q = pre,pre.next  
        while q and q.next:
            if p == q:
                return True
            
            p = p.next
            q = q.next.next 
        
        return False
```



## 总结

核心思路就是快慢指针，记住了就没啥难度，需要注意的循环终止条件判断两个，q.next 和q.next.next，不然有可能遇到q.next已经是空了，q.next.next会报错