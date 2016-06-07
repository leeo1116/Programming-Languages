class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        combination = []
        self.combination_sum_helper(k, n, 1, combination)
        return combination

    def combination_sum_helper(self, k, n, start, combination):
        # combination = []
        for i in range(start, 10):
            if i > n:
                return []
            if k == 1:
                if i == n:
                    return [[i]]
                else:
                    continue
            sub_combination = self.combination_sum_helper(k-1, n-i, i+1, combination)
            if sub_combination:
                sub_combination_len = len(sub_combination)
                for j in range(sub_combination_len):
                    sub_combination[j].insert(0, start)
                    combination.append(sub_combination[j])

        return combination

s = Solution()
print(s.combinationSum3(2, 5))