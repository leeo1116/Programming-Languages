__author__ = 'Liang Li'
class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        weighted_sum = 0
        if "IV" in s:
            weighted_sum -= 2
        if "IX" in s:
            weighted_sum -= 2
        if "XL" in s:
            weighted_sum -= 20
        if "XC" in s:
            weighted_sum -= 20
        if "CD" in s:
            weighted_sum -= 200
        if "CM" in s:
            weighted_sum -= 200

        for c in s:
            if c == 'I':
                weighted_sum += 1
            if c == 'V':
                weighted_sum += 5
            if c == 'X':
                weighted_sum += 10
            if c == 'L':
                weighted_sum += 50
            if c == 'C':
                weighted_sum += 100
            if c == 'D':
                weighted_sum += 500
            if c == 'M':
                weighted_sum += 1000
        return weighted_sum

s = Solution()
print(s.romanToInt("MMCMXXIX"))