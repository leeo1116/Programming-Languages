class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = self.digit_square_sum(n)
        fast = self.digit_square_sum(slow)
        while slow != fast:
            slow = self.digit_square_sum(slow)
            fast = self.digit_square_sum(fast)
            fast = self.digit_square_sum(fast)
        if slow == fast == 1:
            return True
        else:
            return False

    def digit_square_sum(self, n):
        s = 0
        while n:
            s += (n % 10)**2
            n //= 10
        return s

s = Solution()
print(s.isHappy(39))