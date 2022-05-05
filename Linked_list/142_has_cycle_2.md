# 142. 环形链表2

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

## case

![img](https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png)

```
输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)

```
输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```

![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)

```
输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
```

## 思路

141题的升级版，除了要判断链表是否有环以外，如果有环，还需要找到入环的节点。第一反应是快慢指针相遇的节点是不是就是入环点？答案是否定，快慢指针啥时候相遇取决于环有多大；但是入环点确实跟相遇点有联系。

把快慢指针走过的路径分成三段：a表示从开始到入环点的路径；b表示从入环点到相遇点的路径；c表示从相遇点回到到入环点的路径；

当两个指针相遇时，可以得到一个关系：a+b就是慢指针走过的路径；a+b+c+b就是快指针走过的路径；而快指针的路径= 2* 慢指针的路径长度，于是得到等式: `2a+2b = a+b+c+b`,换算得到一个惊人的结论：` a=c`

也就是说，当第一次相遇时，慢指针仍然往前走，此时从head再出发一个指针，和慢指针步伐一致；那么这第三个指针和原来的慢指针，一定会相遇，而且一定在入环点相遇；因为慢指针走过路径c时，第三个指针走过相同的路径a

相遇时，返回慢指针或者第三个指针即可。

这里的第三个指针，仍然可以用原先的fast来表示，看解法：

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return
        
        slow = head.next
        fast = head.next.next
        
        while fast != slow:
            if not fast or not fast.next:
                return 
            slow = slow.next
            fast = fast.next.next
        
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
                
        return slow
```

## 总结

这道题的思路比较好记，但是推到的过程有点难想，如果没有a/b/c三段的分隔不太好得到推论a=c，所以需要额外记忆下这个推导思路

写法上注意是两次循环，第一次相遇里的循环退出条件需要注意，既要判断fast是不是为空，也要判断fast.next是不是为空，否则会由于fast每次走两步报错

还有循环的判断方式，判断fast != slow这种写法比较简洁，比判断fast.next是不是为kong，然后在循环里面再写fast == slow要简单一些