__author__ = 'Liang Li'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total_profit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                total_profit += (prices[i+1]-prices[i])
        return total_profit