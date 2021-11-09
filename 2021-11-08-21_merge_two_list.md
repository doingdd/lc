### case设计

* 有效等价类：两个长度相同，长度不同的list，l1在l2前/后/穿插的情况
* 无效等价类：L1为空，都为空
* 开放类：链表过长？考虑空间占用？是否有环？是否有序等等
```python
case = [
  [(1,2,3),(4,5,6)],
  [(2,4,3),(5,6,4)]
  [(1,3,4),(2)],
  [(4,5,6),(1,2,3)],
  [(),(1,2,3)],
  [(),()]
]
```
### 思路

两个有序链表相加，是很典型的一个双指针的问题，注意利用`有序`这个条件。

可以设定两个指针分别遍历两个链表，遍历的同时比较当前的两个链表的元素，将较小的元素添加到新链表里，并将该指针+1，继续比较，直到其中一个链表结束为止。

结束后，将另一个没遍历完成的链表直接附加到新链表的后面

先写**链表构造**的类和函数，这里只用到了append方法和遍历打印的方法：

```python
#!/usr/bin/python
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None
class ListNode():
    def __init__(self):
        self.head = None

    def append(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            return

        p = self.head
        while p.next:
            p = p.next

        p.next = node

    def pprint(self):
        if not self.head:
            print "Empty"
        p = self.head
        while p:
            print p.val,
            p = p.next

        print ''

def construct_node(l):
    lnode = ListNode()
    for i in l:
        lnode.append(i)

    return lnode


```

然后实现merge的函数，注意遍历完一个listnode之后的处理，和返回值的处理

```python
def merge_list(l1,l2):
    l3 = Node()
    head = l3
    i = l1.head
    j = l2.head
    while i and j:
        if i.val < j.val:
            l3.next = i
            i = i.next
        else:
            l3.next = j
            j = j.next

        l3 = l3.next

    l3.next = i if i else j

    result = ListNode()
    result.head = head.next
    return result

```

调用的部分:

```python
for c in case:
    l1 = construct_node(c[0])
    l2 = construct_node(c[1])
    l3 = merge_list(l1,l2)
    print "case is {0}".format(c)
    print "result is",
    l3.pprint()
输出为：
case is [(1, 2, 3), (4, 5, 6)]
result is 1 2 3 4 5 6 
case is [(2, 4, 3), (5, 6, 4)]
result is 2 4 3 5 6 4 
case is [(1, 3, 4), (2,)]
result is 1 2 3 4 
case is [(4, 5, 6), (1, 2, 3)]
result is 1 2 3 4 5 6 
case is [(), (1, 2, 3)]
result is 1 2 3 
case is [(), ()]
result is Empty

```



### 总结

这道题的思路比较简单，遇到了之后就需要记住，没什么记忆难点，主要难点在于手写链表的实现，包括链表node的初始化，链表的append，链表的打印等等

而且需要注意的是，链表的append正常情况是O(n)的时间复杂度，因为需要遍历到链表末尾，所以，使用普通链表实现的话，这个解法的时间复杂度是O(n^2)



