__author__ = 'Liang Li'
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        dict = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        result = [""]
        for digit in digits:
            lst = dict[digit]
            newresult = []
            for char in lst:
                for str in result:
                    newresult.append(str+char)
            result = newresult
        return result

s = Solution()
print(s.letterCombinations('234'))