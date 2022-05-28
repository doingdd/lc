# [56. 合并区间](https://leetcode.cn/problems/merge-intervals/)

## case

```python
a = ([[1,4],[4,5]],
     [[1,3],[2,6],[8,10],[15,18]],
     [[2,3],[1,2],[3,4],[4,5]],
     [[1,4],[2,3]]
     )
```



## 思路

本题的思路就是排序+合并，首先按照区间开端元素从小到大排序，保证区间开始的有序性，这样只需要判断区间结尾的大小关系，就知道两个区间是该合并还是独立的。排序后，判断两个区间是否合并，有以下几种情况：

1. 后区间的start > 前区间的end，则两区间不重合，分别存放
2. 后区间的start小于前区间的end，这时发生了重合，进一步判断：
   1. 后区间的end也小于前区间的end，说明前区间`包含`了后区间，只保留前区间
   2. 后区间的end大于前区间的end，这时将前区间的end更新为后区间的end,`扩大`其边界

代码的写法，可以将上述几个分支合并一下，下面的分别判断分支的：

```python
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        intervals = sorted(intervals,key=lambda x: x[0])
        for interval in intervals:
            if not res:
                res.append(interval)
            elif res[-1][1] < interval[0]:
                res.append(interval)
            elif res[-1][1] < interval[1]:
                res[-1][1] = interval[1]
            
        return res 
```

下面的合并了一些分支的写法，使用了max函数来判断区间有重合的情况：

```python
def merge_interval(nums):
    nums.sort(key=lambda x:x[0])
    merged = []
    for i in nums:
        if not merged or i[0] > merged[-1][1]:
            merged.append(i)
        else:
            merged[-1][1] = max(merged[-1][1],i[1])

    return merged
```

## 总结

本题的核心思路如果正确，实现比较简单，无非就是是否简洁的问题，核心记忆点:

1. 排序
2. 区间合并的几种情况