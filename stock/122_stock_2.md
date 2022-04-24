# 122. 股票买卖

给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。

在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以先购买，然后在 同一天 出售。

返回 你能获得的 最大 利润 。



## case

```python
case = [
        [7,1,5,3,6,4],
        [1,2,3,4,5],
        [7,6,4,3,1],
        [1,2],
        [],
        [1],
        ]
for i in case:
    print i,maxProfit(i)
```



## 思路

本题没有限制买卖次数，可以交易无限次，那么交易的前提，就是股票比前一天涨价了(加入股票连续涨也涵盖在这里面了，因为连续涨也就是当天卖再当天买，因为题目允许一天买卖无限次)

所以思路很简单，就是只要数组上升，就把上升的差值作为当天的利润计入全局利润中，直到最后一天，如果数组下降，啥也不干

```python
def maxProfit(prices):
    max_profit = 0
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    l = len(prices)
    for i in range(1,l):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]

    return max_profit
```



## 总结

股票系列第二题，无限次买卖的最大利润，只需将每个上升阶段记录累加即可

