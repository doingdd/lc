# 补充24. 双栈排序

给定一个乱序的栈，设计算法将其升序排列。

ps: 允许额外使用一个栈来辅助操作 

> 输入
> [4, 2, 1, 3]
> 输出
> [1, 2, 3, 4]

## case

```python
case = [
        [4,3,2,1],
        [],
        [1,2,3],
        [1,1,1],
        [1],
        [4,2,1,3,4,5],
        [1,2,3,4
```



## 思路

题目要求是对一个栈进行排序，也就是这个栈只有pop和push，然后可以用辅助栈，那么就需要两个栈之间互相倒腾，在遍历原栈的时候，每次都将局部最小的值放入辅助栈中，如果辅助栈顶元素大于当前值，那么需要将辅助栈的元素弹出放回原栈，知道其栈顶元素小于当前值，才可以把当前值放入辅助栈中

```python
def stack_sort(stack):
    tmp_stack = []
    while stack:
        v = stack.pop()
        while tmp_stack and tmp_stack[-1] > v:
            tmp_v = tmp_stack.pop()
            stack.append(tmp_v)
            
        tmp_stack.append(v)
        
    return tmp_stack
    
for i in case:
    print(i)
    print(stack_sort(i))
~                                
```



## 总结

这道题的思路明确了之后，代码还是比较容易实现的，这里需要注意的是：

1. 第一层while循环判断stack是否为空，也就是遍历是否结束
2. 第二层while循环是为了把辅助栈中大于当前值的元素全倒腾回去
3. 同时对tmp_stack进行判空处理，如果为空就直接append即可

这道题感觉很是有种闲的蛋疼的感觉，时间复杂度应该是O(n^2)