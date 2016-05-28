class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """

        max_consecutive_sum, counter, i = 1, 0, 0  # actually initialize max_consecutive_sum to 1 introduces one element
        # the counter should add 1, but it doesn't
        while max_consecutive_sum <= n:
            if i < len(nums) and nums[i] <= max_consecutive_sum:
                max_consecutive_sum += nums[i]
                i += 1
            else:
                max_consecutive_sum += max_consecutive_sum
                counter += 1  # for the last operation (max_consecutive_sum is greater than n before this line)
                # the counter doesn't need to add 1, but it does
        return counter


s = Solution()
print(s.minPatches([9], 10))
