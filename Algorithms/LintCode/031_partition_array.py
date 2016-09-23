class Solution(object):
    def partition_array(self, nums, k):
        left, right = 0, len(nums) - 1
        while left < right:
            # left <= right accounts for the case when all elements are smaller than k
            while left <= right and nums[left] < k:  # when num[left] >= k, stop
                left += 1
            while left < right and nums[right] >= k: # only when num[right] < k, stop
                right -= 1
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        return left

s = Solution()
print(s.partition_array([3, 1, 6, 4, 5], 4))