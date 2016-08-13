__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute1(self, nums):
        permutation = []
        self.dfs(nums, 0, permutation)
        return permutation

    def dfs(self, nums, index, permutation):
        if index == len(nums):
            permutation.append(nums)
        else:
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                self.dfs(nums, index+1, permutation)
                nums[i], nums[index] = nums[index], nums[i]

    def permute(self, nums):
        if len(nums) == 1:
            return [nums]
        permutation = []
        for i in range(len(nums)):
            for p in self.permute(nums[:i]+nums[i+1:]):
                permutation.append([nums[i]]+p)
        return permutation

s = Solution()
print(s.permute([1, 2, 3]))