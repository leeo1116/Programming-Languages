__doc__ = """
Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""

class Solution(object):
    def __init__(self, index):
        self.index = index

    def regular_expression_matching(self, s, p):
        """
        Consider MATCHED case
        Case 1: p[-1] == '*'

            Case 1.1: s[-1] == p[-2] or p[-2] == '.'
                Case 1.1.1: '*' matches 0 times of preceding character
                        ==> check if s matches p[:-2]
                Case 1.1.2: '*' matches 1 times of preceding character
                        ==> check if s[:-1] matches p[:-2].
                        Optimization: check if s[:-1] matches p, this will convert to next round '*' matches 0 times
                        problem, and it will check if s matches p[:-2]
                Case 1.1.3: '*' matches more than 1 times of preceding characters
                        ==> check if s[:-1] matches p

            Case 1.2: s[-1] != p[-2] and p[-2] != '.'
                '*' must match 0 times of preceding character
                ==> check if s matches p[:-2]


        Case 2: p[-1] != '*'
            Case 2.1: p[-1] == '.' or s[-1] == p[-1]
                ==> check if s[:-1] matches p[:-1]
            Case 2.2:
                ==> return False
        :param s: input string
        :param p: input pattern
        :return: bool
        """
        if not p:
            return not s
        if p[-1] == '*':
            if s and (s[-1] == p[-2] or p[-2] == '.'):
                return self.regular_expression_matching(s, p[:-2]) or self.regular_expression_matching(s[:-1], p)
            else:
                return self.regular_expression_matching(s, p[:-2])
        else:
            if s and p[-1] == '.' or p[-1] == s[-1]:
                return self.regular_expression_matching(s[:-1], p[:-1])
            else:
                return False
