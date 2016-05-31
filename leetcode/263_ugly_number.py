class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        for n in [2, 3, 5]:
            if num and num % n == 0:
                return self.isUgly(num/n)
        return False


s = Solution()
print(s.isUgly(0))