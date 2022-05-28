# 150.逆波兰表达式 & 剑指II 036.后缀表达式

有效的算符包括 +、-、*、/ 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

注意 两个整数之间的除法只保留整数部分。

可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

## case

```python
示例 1：

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9
示例 2：

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6
示例 3：

输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```

## 思路

后缀表达式的定义可以总结为：操作数在前，运算符在后，比如ab*表示的是`a*b`，ab+c-表示的是`a+b-c`等等，也就是说，每个运算符都往前找两个数字作为它的操作数，代码思路也是如此，用**一个栈**来存储中间结果，检测到数字就入栈，检测到符号就把栈顶元素弹出两次，第一次弹出的是右操作数，第二次弹出左操作数(注意顺序，不然除法会错)，遍历完成后，栈中元素一定只有一个(默认表达式恒有效)，即为最后答案

```python
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i in '+-*/':
                b = stack.pop()
                a = stack.pop()
                c = int(eval('{0}{1}{2}'.format(a,i,b)))
                stack.append(c)
            else:
                stack.append(int(i))

        return stack[0]
```

## 总结

本题思路就是栈和逆波兰表达式的定义，比较清晰，需要注意三点：

1. 弹出两次栈的左右操作数顺序一定不能搞混，否则除法的操作数和被操作数反了就错了
2. python2的负数除法是地板除(floor),即6/-121 = -1，而不是想象中的0，所以本题是用python3写的
3. 如果必须不能用eval，本题写法就比较复杂，需要判断加减乘数的字符对应的函数，在python中分别是add，sub，mul，除法特殊：lambda x,y: int(x/y)