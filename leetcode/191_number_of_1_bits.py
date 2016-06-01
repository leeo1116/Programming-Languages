class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        weight = 0
        while n:
            n &= (n-1)
            weight += 1
        return weight


s = Solution()
print(s.hammingWeight(7))