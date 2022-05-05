# 712. 删除的最小ascii字符和

## 用例

```python
case = [
  ["sea","eat"],
  ["delete","leet"],
  ["a",""],
  ["a","b"]
]
```



## 思路

这道题乍一看，需要得到的答案是ascii码的值，每个字符都不一样，不能按照题目1143和题目583那种，先求公共子序列，再计算答案的方式了，labuladong的解法也是需要dp table记录删除的ascii字符的数字码，但是，其实仍然可以使用前两题的方式，先求出最大子序列，只不过dp里存放的是最大子序列的ascii码值的和，然后最终再算出两个字符串的总ascii值，减去这个dp[m]\[n]*2

```python
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m,n = len(s1),len(s2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + ord(s1[i-1])
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])
        total = sum([ord(i) for i in s1+s2])
        print total
        print dp[m][n]
        return total - 2 * dp[m][n]
```



## 总结

这道题，除了1143题中基础的求公共子序列的部分以外，需要注意的是其变化，即dp table里存ascii码的值(最大值，总值减最大值即为最小值)，所以，在状态转移的时候，需要dp[i-1]\[j-1] + 上ord(s1[i-1]), 而不是直接+1了