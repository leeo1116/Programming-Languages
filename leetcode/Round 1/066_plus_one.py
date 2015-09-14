__author__ = 'Liang Li'
class Solution:
    # @param {integer[]} digits
    # @return {integer[]}
    def plusOne(self, digits):
        carry_in = (len(digits)-1)*[0]+[1]
        for i in range(len(digits)-1, -1, -1):
            if digits[i]+carry_in[i] == 10 and i > 0:
                carry_in[i-1] = 1
                digits[i] = 0
            elif digits[i]+carry_in[i] == 10 and i == 0:
                digits[i] = 0
                digits = [1]+digits
            else:
                digits[i] = digits[i]+carry_in[i]
        return digits

s = Solution()
print(s.plusOne([9, 9, 6]))
