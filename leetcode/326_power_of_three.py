class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n == 1 or (n % 3 == 0 and self.isPowerOfThree(n / 3))

    def is_power_of_three_iterative(self, n):
        while n > 1 and n % 3 == 0:
            n /= 3
        return n == 1


