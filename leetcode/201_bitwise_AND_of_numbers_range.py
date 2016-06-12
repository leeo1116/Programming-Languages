class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while n > m:
            n &= n-1
        return m&n

s = Solution()
print(s.rangeBitwiseAnd(5, 7))