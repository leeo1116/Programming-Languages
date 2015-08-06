__author__ = 'liangl2'
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        current_max_sum, global_max_sum = 0, -(1 << 31)
        for num in nums:
            current_max_sum = max(current_max_sum+num, num)  # Note: current sum is different from current max sum
            global_max_sum = max(current_max_sum, global_max_sum)
        return global_max_sum

s = Solution()
print(s.maxSubArray([8,-19,5,-4,20]))

