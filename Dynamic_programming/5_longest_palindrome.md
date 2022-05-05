# 5. 最长回文子串

给你一个字符串 `s`，找到 `s` 中最长的回文子串。

## case

```python
case = ["abba",'a','aa','','abc','abccba','abbcdc','abbcd','babad','cbbd']
for i in case:
    print i,longest_s(i)
    
abba abba
a a
aa aa
 0
abc a
abccba abccba
abbcdc cdc
abbcd bb
babad bab
cbbd bb
```



## 思路

### 中心扩散

这道题的中心扩散法比较好理解，就是每次要从当前元素扩散，和从当前元素与下一元素扩散，需要扩散两次，扩散两次的目的就是为了兼容回文串的两种形式: aba或abba

需要注意的是在扩散函数中，需要考虑好退出循环的条件，往左或往右超出边界，或者左右两个元素不相等，返回的时候注意指针的移位，不要返回无效的超出边界的指针即可

比较好理解的中心扩散法，理论上时间复杂度O(n^2)

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def find_s(s,i,j,l):
            while i >= 0 and j < l and s[i] == s[j]:
                i -= 1
                j += 1
            return i+1, j-1

        res = []
        l = len(s)
        max_left,max_right = 0,0
        if not s:
            return 0

        for i in range(l):
            left1,right1 = find_s(s,i,i,l)
            left2,right2 = find_s(s,i,i+1,l)
            if right1-left1 > max_right-max_left:
                max_left,max_right = left1,right1
            if right2-left2 > max_right-max_left:
                max_left,max_right = left2,right2
        
        return s[max_left:max_right+1]
```

## 动态规划

中心扩散实际上包含了很多重复计算，每次扩散之后，在下一个元素重新扩散时，其实有一部分结果已经在前面计算了，有重复，动态扩散的思路实际上就是利用dp table来缓存这一部分的计算结果，用空间换时间，但是本题奇怪的是，用了动态规划，时间复杂度仍然是O(n^2)。。。

本题其实是一个二维的动态规划，二维数组中的value存放是布尔值，表示该索引位置的字符串是否是回文，可以得到对角线肯定为True，因为`dp[i][i]`就是单个元素，一定是回文的

```python
to be done
```







## 总结



