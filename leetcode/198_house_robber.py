class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        total_robbed_even, total_robbed_odd = 0, 0
        for i in range(nums_len):
            if i % 2:
                total_robbed_odd = max(total_robbed_odd+nums[i], total_robbed_even)
            else:
                total_robbed_even = max(total_robbed_even+nums[i], total_robbed_odd)
        return max(total_robbed_even, total_robbed_odd)