#!/usr/bin/python
def maxProfit(prices):
    max_profit = 0
    if len(prices) < 2:
        return 0
    l = len(prices)
    for i in range(1,l):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    
    return max_profit



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
