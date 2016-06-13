class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]*(n)
        w2 = w3 = w5 = 0
        for i in range(1, n):
            ugly[i] = min(ugly[w2]*2, ugly[w3]*3, ugly[w5]*5)
            if ugly[i] == ugly[w2] * 2:
                w2 += 1
            if ugly[i] == ugly[w3] * 3:
                w3 += 1
            if ugly[i] == ugly[w5] * 5:
                w5 += 1
        return ugly[n-1]