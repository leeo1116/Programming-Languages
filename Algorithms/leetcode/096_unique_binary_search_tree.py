__author__ = 'Liang Li'
class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        """
        Assuming the num is 1, 2, 3, ..., k, ..., n
        If use k as the root, there are F(k) = F(k-1)*F(n-k) ways
        The total num will be F(n) = F(0)*F(n-1)+F(1)*F(n-2)+F(2)*F(n-3)+...+F(k-1)*F(n-k)+...+F(n-1)*F(0)
        :param n:
        :return:
        """
        F = [0]*(n+1)
        F[0] = F[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                F[i] += F[j]*F[i-j-1]
        return F[n]

s = Solution()
print(s.numTrees(3))
