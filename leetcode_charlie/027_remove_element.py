__doc__ = """
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""


class Solution(object):
    def __init__(self):
        pass

    def remove_element(self, nums, val):
        nums_len = len(nums)
        j = 0
        for i in range(nums_len):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


s = Solution()
print(s.remove_element([4, 6], 4))
