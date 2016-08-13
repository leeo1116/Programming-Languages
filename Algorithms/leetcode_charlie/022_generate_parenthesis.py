__doc__ = """
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""


class Solution(object):
    def __init__(self):
        pass

    def generateParenthesis(self, n):
        return self.generate_parenthesis(n, n, '', [])

    def generate_parenthesis(self, left, right, p, parenthesis):
        """
        General backtracking algorithm.
        Use left, right to denote the number of remaining left and right parenthesis respectively
        Use p to store each possible parenthesis combination, parenthesis to store all the combinations

        :param left:
        :param right:
        :param p:
        :param parenthesis:
        :return:
        """
        if not right:
            parenthesis.append(p)
        if left:
            self.generate_parenthesis(left-1, right, p+'(', parenthesis)
        if right > left:
            self.generate_parenthesis(left, right-1, p+')', parenthesis)
        return parenthesis


s = Solution()
print(s.generateParenthesis(2))


