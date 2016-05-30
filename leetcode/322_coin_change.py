class Solution(object):
    # DP
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coin_num = [amount+1]*(amount+1)
        coin_num[0] = 0
        for coin in coins:
            for a in range(coin, amount+1):
                coin_num[a] = min(coin_num[a], coin_num[a-coin]+1)

        return coin_num[amount] if coin_num[amount] <= amount else -1


    # Recursion
    def coin_change_dfs(self, coins, amount):
