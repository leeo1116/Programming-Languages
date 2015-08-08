__author__ = 'liangl2'
import math
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def getPermutation(self, n, k):
        array = [x for x in range(1, n+1)]
        k = (k % math.factorial(n)) - 1
        permutation = []
        for i in range(n - 1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            permutation.append(array.pop(idx))

        return "".join(map(str, permutation))

s = Solution()
print(s.getPermutation(8, 77))