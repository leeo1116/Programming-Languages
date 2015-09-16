__author__ = 'Liang Li'
class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        # Considering digits = '2' as an example, possible combinations are ['a', 'b', 'c']. If digits = '23', then
        # combinations are ['a', 'b', 'c']+'d', ['a', 'b', 'c']+'e', ['a', 'b', 'c']+'f'. ETC.
        num_letter_map = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        combinations = ['']
        if not digits:
            return []
        for digit in digits:
            combinations_tmp = []
            for char in num_letter_map[digit]:
                for c_str in combinations:
                    combinations_tmp.append(c_str+char)
            combinations = combinations_tmp
        return combinations

class Solution_recursive:
    def letterCombinations_recursive(self, digits):
        combinations = []
        num_letter_map = {"1":"", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs","8":"tuv","9":"wxyz","10":" "}
        if not digits:
            return []  # can return [''] and delete the next 3 lines, but digits = [], it should return [] instead of ['']
        current_combinations = self.letterCombinations_recursive(digits[1:])
        if not current_combinations:
            current_combinations = ['']
        for c_str in current_combinations:
            for char in num_letter_map[digits[0]]:
                combinations.append(c_str + char)
        return combinations

s = Solution_recursive()
print(s.letterCombinations_recursive(''))