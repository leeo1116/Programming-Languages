class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        combination = []
        return self.combination_sum_helper(k, n, 1, combination)

    def combination_sum_helper(self, k, n, start, combination):
        if n == start:
            return [[start]]
        if k == 0:
            return [[]]

        for i in range(start, 10):
            if k:
                comb = self.combination_sum_helper(k-1, n-i, i+1, combination)
            else:
                comb = self.combination_sum_helper(k, n, i+1, combination)
            for c in comb:
                combination.append([i]+c)
        return combination


s = Solution()
print(s.combinationSum3(2, 7))