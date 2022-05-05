# 剑指30. 包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈的最小元素的 min 函数在该栈中，调用 min、push 及 pop 的时间复杂度都是 O(1)。

示例:

```python
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.min();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.min();   --> 返回 -2.
```

## 思路

本题的点在于如何维护min值，尤其是再 pop了当前min值之后，如何`恢复`以前的min值，所以需要额外一个辅助栈来记录所有min值的`轨迹`

```python
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
       
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        
        tmp_min = min(self.min_stack[-1],x) if self.min_stack else x
        self.min_stack.append(tmp_min)

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.min_stack.pop()


    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def min(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
```



## 总结

这道题虽然写法简单，但是如果没有遇到过，还是很容想简单的，比如只用一个栈位数元素，忘记了min值的变化处理

`tmp_min = min(self.min_stack[-1],x) if self.min_stack else x` 这句是重点