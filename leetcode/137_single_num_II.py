__author__ = 'Liang Li'
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b0, b1 = 0, 0
        for num in nums:
            b0 ^= num & ~b1
            b1 ^= num & ~b0
        return b0

s = Solution()
print(s.singleNumber([1, 1, 1, 2, 3, 2, 2, 4, 4, 4]))
