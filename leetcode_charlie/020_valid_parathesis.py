__doc__ = """
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):
    def __init__(self):
        pass

    def valid_parathesis(self, s):
        """
        :type s: str
        :rtype: bool
        """
        p_dict = {'}': '{', ']': '[', ')': '('}
        p_stack = []
        for c in s:
            if p_stack and p_dict.get(c, None) == p_stack[-1]:
                p_stack.pop()
            else:
                p_stack.append(c)
        return not p_stack


s = Solution()
print(s.valid_parathesis(''))
