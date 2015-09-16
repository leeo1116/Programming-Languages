__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self, nums):
        i = reach = 0
        while i < len(nums) and i <= reach:
            reach = max(reach, nums[i]+i)
            i += 1
        return i == len(nums)

s = Solution()
print(s.canJump([0]))