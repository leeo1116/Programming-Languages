__author__ = 'liangl2'
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return nums
        return self.permute(sorted(nums))

    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        permutation = []
        pre_num = None
        for i in range(len(nums)):
            if nums[i] != pre_num:
                pre_num = nums[i]
                for p in self.permute(nums[:i]+nums[i+1:]):
                    permutation.append([nums[i]]+p)
        return permutation

s = Solution()
print(s.permuteUnique([3,3,1,2,3,2,3,1]))