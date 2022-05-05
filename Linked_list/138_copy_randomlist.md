# 138 复制随机链表



## 用例

使用数组来表示一个链表，每个节点也是一个数组，元素分别为next和random，经过构造，得到一个带random元素的链表

```python
head = [[7,None],[13,0],[11,4],[10,2],[1,0]], 输出和输入一样
head = [[1,1],[2,1]]
head = [[3,None],[3,0],[3,None]]
head = []
head = [[3,3]]
```





## 思路

首先理解随机链表的定义：

```python
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
```

也就是说出去传统的val和next这两个属性外，多了一个random，指向一个随机的node

两次遍历，第一次将每个节点的后面都新增一个value一模一样的节点，新节点和源节点的区别仅在云random没有设置；

第二次遍历将新节点的random指定完成，每个新节点的random都是源节点random的next

第三步，将新节点从原链表中拆出来，并返回

这道题的思路比较绕，这种三步式的解法写起来也比较绕，需要逻辑很清晰，尤其是设计到链表新增节点，删除节点的操作，要注意顺序

```python
   def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        exists = {}
        p = head
        while p:
            new_node = Node(p.val)
            new_node.next = p.next
           
            p.next = new_node
            p = p.next.next
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next 
            
            p = p.next.next 
        
        p = head
        new_p = new_head = Node(-1)
        while p:
            new_p.next = p.next
            new_p = new_p.next
            p.next = new_p.next
            p = p.next
            

        return new_head.next 
```



## 总结

这道题有几个点需要注意：

1. 三步式思路，第一步只copy节点，但是random置空不管；第一步只操作random，但是需要判断原节点的random是否为空，为空不需要操作；第三步是节点拆分，这里使用了一个新的链表new_head来存储,返回时注意把头结点去掉
2. 需要注意的是链表节点的添加：node.next = p.next -> p.next = node -> p = p.next.next这三步顺序；链表节点的删除：p.next = p.next.next -> p = p.next核心是这两步

