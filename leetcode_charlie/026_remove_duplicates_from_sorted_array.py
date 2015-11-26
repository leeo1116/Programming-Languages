__doc__ = """
 Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't
matter what you leave beyond the new length.
"""


class Solution(object):
    def __init__(self, s):
        print(s)

    def remove_duplicates_from_sorted_array(self, nums):
        nums_len = len(nums)
        if nums_len < 2:
            return nums_len
        j = 1
        for i in range(1, nums_len, 1):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1
        return j

s = Solution("Hi")
print(s.remove_duplicates_from_sorted_array([]))