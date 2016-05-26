class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        max_num = nums[0]
        for num in nums:
            max_num = num if num > max_num else max_num

        min1 = min2 = max_num
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        return False

s = Solution()
print(s.increasingTriplet([2,4,-2,-3]))

