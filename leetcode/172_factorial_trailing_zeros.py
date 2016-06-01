class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        zeros_num = 0
        i = 5
        while n//i:
            zeros_num += n//i
            i *= 5
        return zeros_num

s = Solution()
print(s.trailingZeroes(0))
