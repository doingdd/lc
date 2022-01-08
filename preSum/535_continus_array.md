# 525. 连续数组

给定一个二进制数组 `nums` , 找到含有相同数量的 `0` 和 `1` 的最长连续子数组，并返回该子数组的长度。

## case

```python
case = [
  [0,1],
  [0,1,0],
  [0],
  [0,1,1,0]
]
```



## 思路

本题是典型的前缀和题目，先要了解前缀和的思路：把每一个index作为k，sum(nums[0:index])作为value，组成的一个数组就是前缀和，相当于每个位置上存放的是它向前累加的和，这个数组的好处，就是可以省去重复计算，也相当于一个dp table了，空间换时间

本题中，0和1的个数相等，隐含了一个条件：如果把0看成-1，1看成1，当两个index上的前缀和相等时，这两个index中间的序列相当于没加也没减，即子序列和为0，而子序列和为0只有一种可能：0和1的个数一样，正负抵消了

所以，本题中，判断是否为连续数组，就转换成了判断两个index上的对应前缀和是否相等

而且，还可以进一步简化，压根不用存储前缀和了，只用一个变量count表示当前的和，用一个dict存储所有count值以及index的对应关系，只要dict存在count，那么认为两个index上的前缀和相等，这时用当前index减去dict中的index，即可得到子序列的长度

```python
	 def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        count = 0
        sum_dict = {0:-1}
        for i,v in enumerate(nums):
            if v:
                count += 1
            else:
                count -= 1
            if count in sum_dict:
                max_len = max(max_len,i - sum_dict[count])
            else:
                sum_dict[count] = i 
        
        return max_len
```



## 总结 

这道题有两次转化：

1. 0看成-1，这时前缀和相等时的index之差就是子序列长度(当然，如果0不看成-1的话，就不能这么判断了)
2. 直接用count+dict存储，count相当于实现了前缀和，dict实现了记录所有以”和“为key，”index“为value的可能

这道题就死记硬背吧，没碰见过的单靠自己基本不可能想出来

