class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_prod = nums[0]
        imax = imin = max_prod
        for i in range(1, len(nums)):
            # swap imax and imin if current number is negative
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp
            imax = max(nums[i], imax*nums[i])
            imin = min(nums[i], imin*nums[i])
            max_prod = max(max_prod, imax)
        return max_prod

s = Solution()
print(s.maxProduct([1, 2, -4, 5, 6]))