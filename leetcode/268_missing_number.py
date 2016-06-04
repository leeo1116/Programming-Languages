class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Solution 1
        # sum1 = 0
        # for num1 in nums:
        #     sum1 += num1
        # sum2 = (0 + len(nums)) * (len(nums) + 1) / 2
        # return sum2 - sum1

        # Solution 2
        # sum1 = sum2 = 0
        # for num1 in nums:
        #     sum1 += num1
        #
        # for num2 in range(len(nums)+1):
        #     sum2 += num2
        #
        # return sum2-sum1

        # Solution 3
        xor = 0
        for num in nums:
            xor ^= num

        for i in range(len(nums)+1):
            xor ^= i

        return xor

s = Solution()
print(s.missingNumber([0, 1, 4, 5, 2, 3, 8, 7]))