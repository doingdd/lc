# 1047 删除字符串中重复字符



## case

```python
case = [
  "abbaca",
  "aa",
  "abc",
  "abccba",
  "",
  "a",
  "abcabc"
]
```



## 思路

属于类似对对碰的问题，第一个想到用的就是栈，和括号匹配的那道题很像，核心思路就是遍历的时候，用一个栈来存放之前遍历过的元素，判断当前元素如果和栈顶元素相等，则pop，如果不相等则push，最后返回栈中剩余元素

```python
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in s:
            if stack and i == stack[-1]:
                stack.pop()
            else:
                stack.append(i)
            
        return ''.join(stack)
```



## 总结

对对碰问题，想到用栈，唯一注意的点是，注意栈空时候的判断