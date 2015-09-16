__author__ = 'Liang Li'
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit1 = 0
        max_profit2 = 0
        min_price1 = (2 << 31)-1
        min_price2 = (2 << 31)-1
        for price in prices:
            max_profit2 = max(max_profit2, price-min_price2)
            min_price2 = min(min_price2, price-max_profit1)
            max_profit1 = max(max_profit1, price-min_price1)
            min_price1 = min(min_price1, price)
        return max_profit2