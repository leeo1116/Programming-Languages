class Solution(object):
    def combination_sum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.dfs_search(candidates, 0, target)

    def dfs_search(self, candidates, start, target):
        if target == 0:
            return [[]]

        solution_list = []
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            for r in self.dfs_search(candidates, i, target-candidates[i]):
                solution_list.append([candidates[i]]+r)
        return solution_list

s = Solution()
print(s.combination_sum([2, 3, 6, 7, 7, 8], 7))