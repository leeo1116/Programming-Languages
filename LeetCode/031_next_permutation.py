__author__ = 'liangl2'
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        nums_len = len(nums)
        if nums_len <= 1:
            return nums
        for i in range(nums_len-1, 0, -1):
            if nums[i-1] <= nums[i]:
                partition_num = nums[i-1]
                partition_index = i-1
        for i in range(nums_len-1, -1, -1):
            if nums[i] >= partition_num:
                change_num = nums[i]
                change_index = i
        tmp = nums[change_index]
        nums[change_index] = nums[partition_index]
        nums[partition_index] = tmp

        reversed(nums[partition_index+1:])
        return nums

s = Solution()
print(s.nextPermutation([3, 2, 1]))
