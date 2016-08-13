__author__ = 'liangl2'
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
        candidates.sort()
        return self.search(candidates, 0, target)

    def search(self, candidates, start, target):
        if target == 0:
            return [[]]
        res = []
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                break
            for r in self.search(candidates, i, target-candidates[i]):
                res.append([candidates[i]]+r)
        return res