__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        m, n = 0, len(nums)-1
        i = 0
        while i <= n and m <= n:
            if nums[i] == 0:
                nums[m], nums[i] = nums[i], nums[m]
                m += 1
                i += 1
            elif nums[i] == 2:
                nums[n], nums[i] = nums[i], nums[n]
                n -= 1
            else:
                i += 1
        return nums

s = Solution()
print(s.sortColors([0, 1]))