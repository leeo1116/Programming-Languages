class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """


    def combination_sum_helper(self, k, n, combination):
        if n == 0:
            combination.append