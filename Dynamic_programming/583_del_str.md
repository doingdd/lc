# 583 两个字符串的删除操作

## 用例

```python
case = [
  ["sea","eat"],
  ["abc","ab"],
  ["abc","c"],
  ["",""]
  ["aba","abca"],
  ["abc",""],
  ["abc","def"]
]
```



## 思路

这道题其实是1143，最大子序列长度那道题的姐妹题，本题中要求是删除的步数，使两个字符串相等，其实就是对两个字符串分别删除，直到删除剩下的字符串，是它们的最大子序列为止，比如case1中，sea和eat的最大子序列是ea, 那其实删除的步数就等于两个字符串的长度和-2*(子字符串长度)，所以这道题完全可以复制1143这道题的解法，只是最后返回值变了一下

按照1143的解法如下：

```python
   def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [ [0]*(n+1) for _ in range(m+1) ]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])

        print  dp[m][n]

        return m+n - 2*dp[m][n]
```



## 总结

注意的点同1143题

