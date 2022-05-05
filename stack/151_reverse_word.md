# 151.颠倒字符串里的单词



## case

```python
case = [
    "the sky is blue",
    "  hello world ",
    "a good    example"
    ""
]
```

## 思路

说到反转，可以用栈来解决，栈的先进后出的特性恰好是顺序颠倒的，本题里用list模拟一个栈。

虽然单词的顺序反转，但是单词本身不反转，那么需要一个临时的变量word，来存储当前遍历到的单词，到遇到空格时，则认为前面的为一个完整单词，将word入栈，并将word清空

```python
def reverse_word(s):
    stack = []
    word = ""
    for i in s:
        if i==' ':
            if word:
                stack.append(word)
                word = ""
        else:
            word += i

    if word:
        stack.append(word)

    print stack
    return ' '.join(stack[::-1])
```



## 总结

这道题思路比较清晰简单，需要注意两点：

1. 遍历当前字符时，判断其是不是等于`空格`,而不是为空
2. 当遍历到空格时，就将不为空的word入栈，并清空word，这样遇到连续空格不会重复入栈
3. 最后，当结尾不是空格时，还累加了最后一个单词，这是要判断word是不是空，非空则入栈最后一个单词