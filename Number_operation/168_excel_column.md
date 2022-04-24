# 168. Excel 列表名称

给你一个整数 `columnNumber` ，返回它在 Excel 表中相对应的列名称。

例如：

```
A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
```

## case

```python
case = [
        1,28,701,2147483647,

        ]
```



## 思路

这道题别看是个简单题，第一次遇到还是没做出来，要求是将一个数字转化成大写的字母，首先要知道一个字母的转换怎么做，然后再利用移位的方式，计算每一位

1. 单个字母和数字的转换。本题中可以看到转换成单个字母的最大数字是26，对应Z，利用ord('A')=65这个特点，那么1对应65, 2对应66... 注意，本题中的数字是从1开始，在实际转换时，为了移位，需要将数字-1，才能从0开始
2. columnNumber对26取余，(columnNumber-1)%26, 举例，当columnNumber=26时，余数为25，对应的字母则为25+ord('A') = 90,将90转换为字母：chr(90) == 'Z'。这样完成了从`26`到`Z`的转换。由此可以总结，这道题的核心思路，是如何将单个数字转换成想要的字母，这里的转换公式为: chr((n-1)%26 + ord('A'))
3. 然后扩展到每一位上，就是循环判断columnNumber是不是还大于0，如果大于0，就执行第二步，并且将columnNumber /= 26，相当于移位。注意这里的边界条件，即columnNumber如果初始就小于26，循环是可以进入一次的。如果columnNumber最后=0时，也保证=0的当次循环也进入了，不会漏掉边界值

```python
def convert(columnNumber):
    def i2a(i):
        return chr(i+64) if i < 26 else None

    res = ''

    while columnNumber > 0:
        columnNumber -= 1
        res = chr(columnNumber%26 + 65) + res
        columnNumber /= 26

    return res



case = [
        1,28,701,2147483647,

        ]

for i in case:
    print i,convert(i)
```

```python
1 A
28 AB
701 ZY
2147483647 FXSHRXW
```



## 总结

这道题虽然简单，但是很容易翻车，注意的点：

1. 这道题相当于进制转换，但是是从1开始的(1对应A)，这给单个数字和字母的转换带来了一个额外的计算，即将数字-1之后再转换
2. 单个字母的转换，需要提前尝试下，如何将26对应成Z
3. 多重循环时的边界条件，比如columnNumber初始小于26时，初始等于0时等，本题直接将columnNumber>0设为循环条件，实际上是cover了这些边界条件的