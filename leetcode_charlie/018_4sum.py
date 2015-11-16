__doc__ = """
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique
quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        if nums_len < 4:
            return []
        nums = sorted(nums)
        solution_set = set()
        for i in range(nums_len):
            target3 = target-nums[i]
            for j in range(i+1, nums_len-2):
                k = j+1
                l = nums_len-1
                # if nums[j] != nums[j-1]:
                while k < l:
                    sum3 = nums[j]+nums[k]+nums[l]
                    if sum3 < target3:
                        k += 1
                    elif sum3 > target3:
                        l -= 1
                    else:
                        solution_set.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
        return list(solution_set)

s = Solution()
print(s.fourSum([0, 0, 0, 0], 0))


