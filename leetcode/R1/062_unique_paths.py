__author__ = 'liangl2'
class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        N = n + m - 2
        k = m - 1
        return self.c_n_k(N, k)

    def c_n_k(self, n, k):
        c = 1
        for i in range(1, k+1):
            c = c*(n-k+i)/i
        return c

s = Solution()
print(s.uniquePaths(4, 3))