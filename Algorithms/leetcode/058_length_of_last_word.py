__author__ = 'Liang Li'
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLastWord(self, s):
        if s == '':
            return 0
        m = n = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if m != n:
                    return n-m
                m += 1
                n = m
            else:
                n += 1
            if i == 0:
                return n-m

s = Solution()
print(s.lengthOfLastWord(""))
