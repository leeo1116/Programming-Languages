class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        product = [0]*nums_len
        left = right = 1
        for i in range(nums_len):
            if i > 0:
                left = nums[i-1]*left
            product[i] = left

        for j in range(nums_len-1, -1, -1):
            if j < nums_len-1:
                right = nums[j+1]*right
            product[j] *= right

        return product

