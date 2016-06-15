class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        sub_sum = i = 0
        sub_len = len(nums)+1
        for j in range(len(nums)):
            sub_sum += nums[j]
            while sub_sum >= s:
                sub_len = min(sub_len, j-i+1)
                sub_sum -= nums[i]
                i += 1
        return sub_len if sub_len <= len(nums) else 0