__author__ = 'liangl2'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single_num = 0
        for num in nums:
            single_num ^= num
        return single_num