__author__ = 'Liang Li'
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1
        sum0 = 0
        n = len(nums)
        neg_num = 1
        sum1 = int((1+n)*n/2)
        for i in range(len(nums)):
            sum0 += nums[i]
            if nums[i] <= 0:
                neg_num = nums[i]
        if neg_num == 1:
            if  > 1:
                return nums[0]-1
            return n+1

        return neg_num+(sum1-sum0)


s = Solution()
print(s.firstMissingPositive([]))