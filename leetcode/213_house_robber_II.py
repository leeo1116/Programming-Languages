class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Classification 1: consider two neighbors
        i, i+1 can not be robbed at the same time, so either i is not robbed or i+1 is not robbed.
        when i is not robbed, i-1 and i+1 can be any status robbed/un-robbed, it's like the houses are in a line
        when i+1 is not robbed, i and i+2 can be any status robbed/un-robbed, it's like the houses are in a line
        (if both i and i+1 are not robbed, this case is duplicated, but it doesn't affect the final result, because the
        larger money is returned. It can be removed in any one of these two cases, but the larger money keep the same)

        Classification 2: consider arbitrary house i
        i can be robbed or not robbed,
        if i is not robbed, the remaining houses can be robbed in a line fashion
        if i is robbed, then i-1 and i+1 can not be robbed, the remaining n-3 houses can be robbed in a line fashion
        """
        if len(nums) < 3:
            return max([0] + nums)
        max_money1 = self.rob_line_case(nums[1:])  # house 0 is not robbed
        max_money2 = self.rob_line_case(nums[2:-1]) + nums[0]  # house 0 is robbed
        return max(max_money1, max_money2)

    @staticmethod  # if not stated, function can only be called by class
    def rob_line_case(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        total_robbed_even, total_robbed_odd = 0, 0
        for i in range(nums_len):
            if i % 2:
                total_robbed_odd = max(total_robbed_odd + nums[i], total_robbed_even)
            else:
                total_robbed_even = max(total_robbed_even + nums[i], total_robbed_odd)
        return max(total_robbed_even, total_robbed_odd)


s = Solution()
print(s.rob([2, 1, 3, 4, 7, 5, 6]))
