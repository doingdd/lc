# x的平方根

给你一个非负整数 x ，计算并返回 x 的 算术平方根 。

由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。

注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。

## case

```python
case = [
  1,4,8,3,0,10,9,81
]
```

## 思路

本题使用二分查找的方式，left和right初始值分别为0和x本身，每次取中间值作为mid，然后对比mid* mid是比x大还是小(大概率是大)，如果大，就将right缩小到mid-1,如果小，那么有可能它是要找到的答案，也有可能不是，所以设定一个ans，每次mid*mid < target，则将ans= mid，并将left = mid + 1

终止条件需要加上left = right,为什么呢？因为在x=0和x=1时，都会有循环到left=right的时候，如果不加上left=right这一次的话，ans没法更新成最新的

```python
def sqr(x):
    l,r,ans = 0,x,-1
    while l <= r:
        mid = (l+r)//2
        if mid*mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1

    return ans

```



## 总结

这道题属于背下来就会，不背下来很难想的简单题。。核心注意点还是二分的变种，查找第一个大于等于target或者第一个小于等于target的，本题属于后者，第35题属于前者。所以分析题意，在合适的分支里加上对答案的处理非常重要。

