__doc__ = """
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the
array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution(object):
    def __init__(self, index):
        self.index = index

    def three_sum(self, nums):
        num_len = len(nums)
        if num_len < 3:
            return []
        nums = sorted(nums)
        solution_nums = []
        for i in range(num_len):
            j = i+1
            k = num_len-1
            if i == 0 or nums[i] != nums[i-1]:
                while j < k:
                    if nums[j]+nums[k] > 0-nums[i]:
                        num_k = nums[k]
                        k -= 1
                        while j < k and nums[k] == num_k:
                            k -= 1
                    elif nums[j]+nums[k] < 0-nums[i]:
                        num_j = nums[j]
                        j += 1
                        while j < k and nums[j] == num_j:
                            j += 1
                    else:
                        solution_nums.append([nums[i], nums[j], nums[k]])
                        num_j = nums[j]
                        j += 1
                        while j < k and nums[j] == num_j:
                            j += 1

                        num_k = nums[k]
                        k -= 1
                        while j < k and nums[k] == num_k:
                            k -= 1
        return solution_nums


s = Solution(15)
print(s.index)
print(s.three_sum([-1, 0, 1, 2, -1, -4]))

# Or use set() data structure, solution_nums = set(), ... solution_nums.add((nums[i], nums[j], nums[k]))