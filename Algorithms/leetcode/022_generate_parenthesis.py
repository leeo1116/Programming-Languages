__author__ = 'Liang Li'
class Solution:
    # @param {integer} n
    # @return {string[]}

    def generateParenthesis(self, n):
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p,
            return parens
        return generate('', n, n)

    def generate_parenthesis(self, left, right, p='', parenthesis=[]):
        if not right:
            parenthesis.append(p)
        if left:
            self.generate_parenthesis(left-1, right, p+'(')
        if right > left:
            self.generate_parenthesis(left, right-1, p+')')

        return parenthesis

s = Solution()
print(s.generate_parenthesis(3, 3))