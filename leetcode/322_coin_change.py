import timeit


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
        if amount < 1:
            return 0
        count = [0]*amount
        return self.dfs_helper(coins, amount, count)

    def dfs_helper(self, coins, r_amount, count):
        if r_amount < 0:  # Not valid combination
            return -1
        if r_amount == 0:  # Complete
            return 0
        if count[r_amount-1] != 0:  # the count of r_amount exists, then re-use
            return count[r_amount-1]
        min_count = r_amount+1
        for coin in coins:
            c_count = self.dfs_helper(coins, r_amount-coin, count)
            if 0 <= c_count < min_count:
                min_count = c_count+1
        count[r_amount-1] = min_count if min_count != r_amount+1 else -1
        return count[r_amount-1]


s = Solution()
timeit.timeit('s.coinChange([255,196,450,227,98,259,386,36,287,6], 4063)', number=10000)
timeit.timeit('s.coin_change_dfs([255,196,450,227,98,259,386,36,287,6], 4063)', number=10000)
print(s.coinChange([255,196,450,227,98,259,386,36,287,6], 4063))
print(s.coin_change_dfs([255,196,450,227,98,259,386,36,287,6], 4063))