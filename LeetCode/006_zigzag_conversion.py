__author__ = 'liangl2'
class Solution:
    # @param {string} s
    # @param {integer} numRows
    # @return {string}
    def convert(self, s, numRows):
        if len(s) <= numRows or numRows == 1:
            return s
        ss = s[0:numRows]
        rlist = ""
        for i in range(numRows):
            delta_i = 0
            while i+delta_i < len(s):
                rlist += s[i+delta_i]
                if i == 0 or i == numRows-1:
                    delta_i += 2*(numRows-1)
                else:
                    if (i+delta_i) % (2*numRows-2) in range(1, numRows-1):
                        delta_i += 2*(numRows-i-1)
                    else:
                        delta_i += 2*i
        return rlist

s = Solution()
zigzag = s.convert("AB", 1)
print(zigzag)