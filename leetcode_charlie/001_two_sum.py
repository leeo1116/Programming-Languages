__doc__ = """
Given an array of integers, find two numbers such that they add up to a specific target number.The function twoSum
should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
Please note that your returned answers (both index1 and index2) are not zero-based.You may assume that each input would
have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution(object):
    def __init__(self, index):
        self.index = index

    def two_sum(self, nums, target):
        print('#{0} Solution:\n'.format(self.index))
        num_scanned = {}
        for i, num in enumerate(nums):
            if num_scanned.get(target-num, None) is not None:
                return num_scanned[target-num]+1, i+1
            else:
                num_scanned[num] = i

s = Solution(1)
solution = s.two_sum([0, 4, 3, 0], 0)
print(solution)
