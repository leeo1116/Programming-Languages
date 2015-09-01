__author__ = 'liangl2'
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        p_stack = []
        max_len = 0
        for i, char in enumerate(s):
            if char == '(':
                p_stack.append(i)
            else:
                if p_stack and s[p_stack[-1]] == ')':
                    p_stack.append(i)
                elif p_stack and s[p_stack[-1]] == '(':
                    p_stack.pop()
                else:
                    p_stack.append(i)
        if len(p_stack) == 0:
            return len(s)
        # p_stack.append(len(s))
        for i in range(1, len(p_stack)):
            max_len = max(max_len, p_stack[i]-p_stack[i-1])
        max_len = max(p_stack[0]-0, len(s)-p_stack[-1]-1, max_len-1)
        return 0 if max_len < 2 else max_len

s = Solution()
print(s.longestValidParentheses("()()()())"))

