__doc__ = "Liang Li"


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        prices_len = len(prices)
        if prices_len <= 1:
            return 0
        s0 = [0] * prices_len
        s1 = [0] * prices_len
        s2 = [0] * prices_len

        s0[0] = 0
        s1[0] = -prices[0]
        s2[0] = 0

        for i in range(1, prices_len):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]
        return max(s0[prices_len - 1], s2[prices_len - 1])


    def max_profix(self, prices):
        prices_len = len(prices)
        if prices_len <= 1:
            return 0

        s0 = 0
        s1 = -prices[0]
        s2 = 0

        for i in range(1, prices_len):
            last_s2 = s2
            s2 = s1 + prices[i]
            s1 = max(s1, s0 - prices[i])
            s0 = max(s0, last_s2)

        return max(s0, s2)