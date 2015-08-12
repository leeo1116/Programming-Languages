__author__ = 'liangl2'
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        if k == 1:
            return [[i] for i in range(1,n+1)]
        elif k == n:
            return [[i for i in range(1,n+1)]]
        else:
            rs=[]
            rs += self.combine(n-1,k)
            part = self.combine(n-1,k-1)
            for ls in part:
                ls.append(n)
            rs += part
            return rs

s = Solution()
print(s.combine(5, 3))