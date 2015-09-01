__author__ = 'Liang Li'
class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        return [x ^ (x >> 1) for x in range(2**n)]

    def gray_code_0(self, n):
        results = [0]
        for i in range(n):
            results += [x + 2**i for x in reversed(results)]
        return results

s = Solution()
print(s.grayCode(3))