__author__ = 'liangl2'
class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def regular_expression_matching(self, s, p):
        if not p:
            return not s
        """
        Consider Matched Cases:
        Case1: the last character is *
            Case1.1: * matches 0 times of preceding character, in this case s[-1] != p[-2] and p[-2] != '.'
            Case1.2: * matches 1 times of preceding character, in this case s[-1] == p[-2] or p[-2] == '.'
            Case1.3: * matches more than 1 times of preceding character, in this case s[-1] == p[-2] or p[-2] == '.'
        Case2: the last character is not *
            Case2.1: last element in p is '.'
            Case2.2: last element in p == last element in s
        """
        if p[-1] == '*':
            if s and (s[-1] == p[-2] or p[-2] == '.'):
                return self.regular_expression_matching(s, p[:-2]) or self.regular_expression_matching(s[:-1], p)  # Case1.1 or (Case1.2, Case1.3)
            else:
                return self.regular_expression_matching(s, p[:-2])
        else:
            if s and (s[-1] == p[-1] or p[-1] == '.'):
                return self.regular_expression_matching(s[:-1], p[:-1])
            else:
                return False

s = Solution()
is_matched = s.regular_expression_matching("abb", "abb*")
print(is_matched)