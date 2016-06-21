class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 1
        nums = 10
        unique_digits = 9
        available_num = 9
        while n > 1 and available_num > 0:
            unique_digits *= available_num
            available_num -= 1
            n -= 1
            nums += unique_digits
        return nums

s = Solution()
print(s.countNumbersWithUniqueDigits(1))