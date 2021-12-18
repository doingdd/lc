# 23. 合并k个排序链表



## 用例设计

* 有效等价类：lists = [[1,4,5],[1,3,4],[2,6]], 输出: [1,1,2,3,4,4,5,6]
* 特殊值: lists = [],[[]],输出[], [[1],[1],[1],[1]],[[],[1],[2,3]]

```python
case = [
  			[[1,4,5],[1,3,4],[2,6]],
        [],
  			[[]],
  			[[1],[1],[1],[1]],[[],[1],[2,3]],
        [[2,3,4],[5,6,7],[1],[2,3]]
       ]
```



## 思路及解答

这道题实际上是第21题的升级版，21题是合并两个有序链表，这道题升级成k个，核心的思路仍然没有变，只不过用来遍历的指针从`2个`变成了`k个`，而每次遍历时，比较`2个数字的大小`，并添加到新list里，升级成了`从k个数字里选出最小的`,这道题比较难的点主要是各个函数的交互，有很多细节如果不一一对应的话，很难run bug free的代码

### 准备工作

我们需要把输入的case，从列表转化成链表，当然也可以不用这么繁琐，直接按照leetcode的方式，定义Node()即可，但是为了专业(主要是多写写，增加熟练度)，也为了run起来可以有标准的输出，仍然构造了ListNode的pprint方法(虽然后面没有用到)

```python
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class ListNode():
    def __init__(self):
        self.head = None

    def pprint(self):
        if not self.head:
            print "Empty"
        p = self.head
        while p:
            print p.val,
            p = p.next
        print ''

def construct(l):
    ''' transfer list to listnode
    '''
    listnode = ListNode()
    if not l:
        return listnode

    listnode.head = Node(l[0])
    p = listnode.head
    for i in l[1:]:
        node = Node(i)
        p.next = node
        p = p.next

    return listnode

```

### 核心题解

为了代码整洁，定义三个函数，第一个函数merge，用来将case做转化，并将得到的结果打印出来

```python
def merge(c):
    lists = []
    rt_list = []
    for i in c:
        lists.append(construct(i).head)

    new_head = merge_list(lists)
    if not new_head:
        return rt_list
    p = new_head
    while p:
        rt_list.append(p.val)
        p = p.next

    return rt_list
```

第二个函数，其实也是第二层，接收格式为List[Node]的输入，并输出合并后的node

```python
def merge_list(lists):
    '''
    type lists: List(Node)
    type rt: Node
    '''
    k = len(lists)
    if k == 0:
        return None
    if k == 1:
        return lists[0]

    rt = ListNode()
    p = rt.head = Node()
    i = 0
    while True:
        for i in range(k):
            if not lists[i]:
                continue

            min_i,min_v = find_min(lists)
            lists[min_i] = lists[min_i].next
            node = Node(min_v)
            p.next = node
            p = p.next
            break

        else:
            break

    return rt.head.next

```

第三个函数，是用来找到最小值的find_min,为了让指针移动，需要返回最小值的index，以及value

```python
def find_min(lists):
    min_i = 0
    min_v = float('inf')
    for i,l in enumerate(lists):
        if not l:
            continue
        if l.val < min_v:
            min_v = l.val
            min_i = i

    #print min_i,min_v
    return min_i,min_v


for i in case:
    print "case is {0},result is {1}".format(i,merge(i))

```

运行本题的case，得到:

```python
case is [[1, 4, 5], [1, 3, 4], [2, 6]],result is [1, 1, 2, 3, 4, 4, 5, 6]
case is [],result is []
case is [[]],result is []
case is [[1], [1], [1], [1]],result is [1, 1, 1, 1]
case is [[], [1], [2, 3]],result is [1, 2, 3]
case is [[2, 3, 4], [5, 6, 7], [1], [2, 3]],result is [1, 2, 2, 3, 3, 4, 5, 6, 7]
```



## 总结

这道题的解法，应该属于比较暴力的一种，因为find_min的方式是O(k)，再加上lists的从前往后的遍历O(n),其实时间复杂度是O(n*k),但是好处是空间复杂度比较低

另：参考了标准答案之后，本题解还有进一步优化时间的方法：用堆来代替find_min，可以将时间复杂读优化到O(logk*n)