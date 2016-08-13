class Solution(object):
    def combination_sum2(self, candidates, target):
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
            if i != start and candidates[i] == candidates[i-1]:
                continue
            if candidates[i] > target:
                break
            for r in self.dfs_search(candidates, i+1, target-candidates[i]):
                solution_list.append([candidates[i]]+r)
        return solution_list

s = Solution()
print(s.combination_sum2([2, 3, 6, 7, 7, 8], 7))