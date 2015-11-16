__doc__ = """
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
1: None 2: abc 3: def
4: ghi  5: jkl 6: mno
7: pqrs 8: tuv 9: wxyz

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""


class Solution(object):
    def __init__(self):
        pass


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digit_str = {'1':    '',  '2': "abc", '3': "def",
                     '4': 'ghi',  '5': "jkl", '6': "mno",
                     '7': "pqrs", '8': "tuv", '9': "wxyz"}

        combination = ['']
        for d in digits:
            combination_tmp = []
            for c in digit_str[d]:
                for s in combination:
                    combination_tmp.append(s+c)
            combination = combination_tmp
        return combination


s = Solution()
print(s.letterCombinations('23'))
