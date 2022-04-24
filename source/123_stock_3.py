#!/usr/bin/python
def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy1 = buy2 = -prices[0]
    sell1 = sell2 = 0
    for i in prices[1:]:
        buy1 = max(buy1,-i)
        sell1 = max(sell1,buy1+i)
        buy2 = max(buy2,sell1-i)
        sell2 = max(sell2,buy2+i)
        
    return sell2 

case = [
        [3,3,5,0,0,3,1,4],
        [1,2,3,4,5],
        [7,6,4,3,1]
        ]

for i in case:
    print i,maxProfit(i)
