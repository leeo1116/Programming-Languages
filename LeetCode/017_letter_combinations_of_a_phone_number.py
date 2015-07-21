__author__ = 'Liang Li'
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        digit_letter_map = {'1': '', '2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv",
                            '9': "wxyz", '0': ''}
        letter, i = [' ']*len(digits), 0
        for digit in digits:
            letter[i] = digit_letter_map[digit]
            i += 1

s = Solution()
s.letterCombinations('213')