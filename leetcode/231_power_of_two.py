class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and not (n & (n-1))


s = Solution()
print(s.isPowerOfTwo(6))