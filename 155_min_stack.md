# 155. 最小栈

## 用例

输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

这道题属于操作题，case也可以写成列表形式，只不过需要包一层调用

```python
case = [
  ["push",-2],
  ["push",0],
  ["push",-3],
  ["getMin"],
  ["pop"],
  ["top"],
  ["getMin"]
]
result = [None,None,None,-3,None,0,-2]

```





## 思路

这道题需要实现四个方法，push入栈，pop出栈都返回空，top返回栈顶元素，getMin返回最小元素，而且已经约定了后三个方法都在非空栈上调用，所以不用考虑栈为空的情况，当然为了加分也可以考虑，在每个方法执行前判断栈长度即可

第一个想到的就是用python的list来实现，额外维护一个最小值就行了(错误❌，没有考虑pop之后，最小值如何更新的问题)

为了解决pop之后，恢复原有的最小值，则需要将所有的最小值存在一个辅助栈里，这个栈存储的永远是跟最小栈里相对应的最小值

```python
class MinStack():
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self,val):
        self.stack.append(val)
        self.min_value = min(self.min_stack[-1],val)
        self.min_stack.append(self.min_value)

        return

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

        return

    def top(self):

        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

def stack_option(option):
    if len(option) > 1:
        return getattr(stack,option[0])(option[1])
    else:
        return getattr(stack,option[0])()

## 执行
stack = MinStack()
for i,case in enumerate(case):
    output = stack_option(case)
    print case,result[i],output
    assert output == result[i]
```



## 总结

这道题看似简单，但是很容易犯我第一个思路犯的错误，仅用一个变量存储最小值

所以需要注意的点是，在push和pop时，都需要操作两个列表，一个是存储值，另一个存储当前的最小值，pop的时候也是同步操作就可以了

