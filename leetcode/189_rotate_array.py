class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        tmp1 = nums[:nums_len-k]
        tmp2 = nums[nums_len-k:]
        nums[:k] = tmp2
        nums[k:] = tmp1
        print(nums)

s = Solution()
s.rotate([1, 2], 1)