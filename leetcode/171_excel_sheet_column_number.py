class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        p = len(s)
        for char in s:
            num += (ord(char.upper())-ord('A')+1)*26**(p-1)
            p -= 1
        return num


s = Solution()
print(s.titleToNumber(""))