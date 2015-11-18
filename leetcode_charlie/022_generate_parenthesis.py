__doc__ = """
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""


class Solution(object):
    def __init__(self):
        pass

    def generate_parenthesis(self, n):
        left = right = n

