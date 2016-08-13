class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        title = ""
        while n:
            title = chr(ord('A') + (n-1) % 26)+title
            n = (n-1) // 26
        return title


s = Solution()
print(s.convertToTitle(52))