# 2095.删除链表的中间节点

给你一个链表的头节点 head 。删除 链表的 中间节点 ，并返回修改后的链表的头节点 head 。

长度为 n 链表的中间节点是从头数起第 ⌊n / 2⌋ 个节点（下标从 0 开始），其中 ⌊x⌋ 表示小于或等于 x 的最大整数。

对于 n = 1、2、3、4 和 5 的情况，中间节点的下标分别是 0、1、1、2 和 2 。



## case

示例1

![img](https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png)

```python
输入：head = [1,3,4,7,1,2,6]
输出：[1,3,4,1,2,6]
解释：
上图表示给出的链表。节点的下标分别标注在每个节点的下方。
由于 n = 7 ，值为 7 的节点 3 是中间节点，用红色标注。
返回结果为移除节点后的新链表。 
```

示例2.

![](https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png)

```python
输入：head = [1,2,3,4]
输出：[1,2,4]
解释：
上图表示给出的链表。
对于 n = 4 ，值为 3 的节点 2 是中间节点，用红色标注。
```

示例3.

![img](https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png)

```python
输入：head = [2,1]
输出：[2]
解释：
上图表示给出的链表。
对于 n = 2 ，值为 1 的节点 1 是中间节点，用红色标注。
值为 2 的节点 0 是移除节点 1 后剩下的唯一一个节点。
```

## 思路

本题思路可以完全copy第`876.链表的中间节点`的解法，唯一的区别就是该题是为了找出中间节点，所以返回的是p.next；

本题是为了删除中间节点，则需要找到的是中间节点的前一个节点，也就是p,然后将p.next指向p.next.next, 相当于删除(不考虑内存回收的情况，如果考虑，需要将待删除节点的.next指向None，写法上需要一个额外的临时变量来存储)；

用了dummy节点之后非常顺畅，具体不再详述，核心方法就是在纸上多写写每一步骤，根据步骤推出代码

```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        p = dummy
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next 
        
        p.next = p.next.next 
        
        return dummy.next 
```



## 总结

**876和2095**这两道题思路完全一致，核心记忆点：

1.快慢指针，快指针步长是两步，慢指针一步，这样可以找到中间节点

2.奇数长度和偶数长度的链表的情况需要同时考虑，在纸上画，写法不唯一，本题采用快指针指向head，慢指针指向dummy的办法

3.dummy真乃利器，引入后代码简洁，而且基本不用考虑head为空等异常情况

