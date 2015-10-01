__author__ = 'liangl2'
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join([c.lower() for c in s if c.isalnum()])
        # return s == s[::-1]
        i, j = 0, len(s)-1
        while i <= j and s[i] == s[j]:
            i += 1
            j -= 1
        return i > j
s = Solution()
print(s.isPalindrome("ab2a"))