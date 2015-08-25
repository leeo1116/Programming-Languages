__author__ = 'liangl2'
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        sorted(nums)
        permutations = [[]]
        unique_permute(nums, 0, len(nums), permutations)
        return permutations

    def unique_permute(self, nums, i, j, permutations):
        if i == j-1:
