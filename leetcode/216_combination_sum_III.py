class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        return self.combination_sum_helper(k, n, 1)

    def combination_sum_helper(self, k, n, start):
        combination = []
        for i in range(start, 10):
            if i > n/k:
                return combination
            if k == 1:
                if i == n:
                    return [[i]]
                else:
                    continue

            for c in self.combination_sum_helper(k-1, n-i, i+1):
                combination.append([i]+c)
        return combination



s = Solution()
print(s.combinationSum3(3, 9))