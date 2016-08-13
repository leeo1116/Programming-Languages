class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Break n into as many factors as possible, because the power function grows faster than base function
        i.e. a^x > x^a, when x -> +inf
        Assume there exists a factor f, and f >= 4
        it can be further broken into 2*(f-2) that keeps the sum the same, while 2*(f-2) >= f
        So the factors are only 1, 2, 3, since 1 doesn't increase the product, on the contrary, it decreases the product
        Only 2 and 3 are the only factors
        n = 2*i + 3*j
        p = 2^i*3^j, the factors should include as many 3s as possible, because 3^x > 2^x, when x is sufficiently large
        if n = 2*0+3*j, p = 3^j
        if n = 2*1+3*j, p = 2*3^j
        if n = 2*2+3*j, p = 2^2*3^j
        """

        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3**(n//3)
        if n % 3 == 1:
            return 2*2*3**((n-4)//3)
        if n % 3 == 2:
            return 2*3**((n-2)//3)


s = Solution()
print(s.integerBreak(16))
