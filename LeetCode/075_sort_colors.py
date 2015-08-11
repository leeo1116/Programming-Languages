__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        i, j = 0, len(nums)-1
        for num in nums:
            if num == 0:
                nums[i] = 0
                i += 1
            elif num == 2:
                nums[j] = 2
                j -= 1
        return nums

s = Solution()
print(s.sortColors([1, 0, 2, 0, 1, 1, 0, 0, 1, 1, 2, 2, 0, 1, 1]))